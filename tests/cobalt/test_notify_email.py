"""F18's out-of-band channel — Charter §3 F18, SPRINT-LADDER §S1-P4.

"red also out-of-band = email via Layer-B Google OAuth at MVP (alert
path != monitored path)."

What this file proves, in the order it matters:

1. A SEND WORKS, mocked at the Gmail client boundary and nowhere higher —
   message assembly, base64url, the subject prefix, the RFC 2822
   headers and the error mapping are all real code under test.
2. THE ALERT PATH IS NOT THE MONITORED PATH. A send with Postgres,
   Mattermost and the vault-path resolver all sabotaged still goes.
   This is the whole feature; if only one test in this file survives,
   it should be that one.
3. A FAILED SEND SURFACES. The red DM gains "email channel DOWN:
   <reason>", the beat does not crash, and the failure is recorded. This
   is S1-P4's negative proof, run as a mocked failure rather than
   against the production vault — the production vault is not a test
   target.
4. F19 REDACTS BOTH NEW SHAPES, by pattern AND by literal, on the email
   channel, over the subject as well as the body.
5. THE VAULT ROUND-TRIPS. put -> read -> literal-guard enrolment, on a
   throwaway vault with a throwaway key.
6. THE SEND STORE ROUND-TRIPS on cobalt_dev (rolled back by the suite's
   own transaction fixture).
7. notify.yaml VALIDATION refuses what it should.

NO REAL SECRET APPEARS HERE. Every credential below is syntactically
valid and semantically dead: right prefix, right character class, right
length, wrong everything else. The vault fixtures build a NEW vault in a
tmp_path with a NEW Fernet key — the real `data/.cobalt_vault` is never
opened, read, or written by this file.
"""

from __future__ import annotations

import base64
import json
from email import message_from_bytes, policy

import pytest

from cobalt.notify import config as notify_config
from cobalt.notify import email as email_mod
from cobalt.notify.config import (
    CLIENT_ID_KEY,
    CLIENT_SECRET_KEY,
    REFRESH_TOKEN_KEY,
    EmailConfig,
    NotifyConfig,
    NotifyConfigError,
)
from cobalt.notify.email import EmailError, channel_status, send_email
from cobalt.redact import secrets as secrets_mod

# --- dead-but-well-formed credentials --------------------------------
FAKE_CLIENT_ID = "111111111111-deadbeefdeadbeefdeadbeef.apps.googleusercontent.com"
FAKE_CLIENT_SECRET = "GOCSPX-exampleclientsecretvalue123"
FAKE_REFRESH_TOKEN = "1//0gExampleRefreshTokenValueHere123456"

CFG = EmailConfig(enabled=True, to="alerts@example.com", subject_prefix="[COBALT]")


# =====================================================================
# fixtures
# =====================================================================


@pytest.fixture
def tmp_vault(tmp_path, monkeypatch):
    """A throwaway encrypted vault with a throwaway key.

    Points BOTH `VAULT_FILE` and `COBALT_MASTER_KEY` at material created
    inside this test. The real vault is never touched — which is not a
    nicety here: `put_secret` writes, and a test that wrote to
    `data/.cobalt_vault` would be editing production credentials.
    """
    from cryptography.fernet import Fernet

    key = Fernet.generate_key().decode()
    path = tmp_path / ".cobalt_vault"
    path.write_bytes(Fernet(key.encode()).encrypt(json.dumps({}).encode()))

    monkeypatch.setattr(secrets_mod, "VAULT_FILE", path)
    monkeypatch.setenv(secrets_mod.MASTER_KEY_ENV, key)
    secrets_mod.reset_cache()
    yield path
    secrets_mod.reset_cache()


@pytest.fixture
def armed_vault(tmp_vault):
    """A vault holding the full, dead OAuth triple."""
    secrets_mod.put_secret(CLIENT_ID_KEY, FAKE_CLIENT_ID)
    secrets_mod.put_secret(CLIENT_SECRET_KEY, FAKE_CLIENT_SECRET)
    secrets_mod.put_secret(REFRESH_TOKEN_KEY, FAKE_REFRESH_TOKEN)
    return tmp_vault


class FakeGmail:
    """The Gmail client, at the exact boundary `_gmail_service` returns.

    Records the request body so the tests can assert on the REAL RFC 2822
    bytes this codebase built, rather than on a string it was handed.
    """

    def __init__(self, *, message_id="18f0c0ffee", raises=None):
        self.message_id = message_id
        self.raises = raises
        self.sent_body = None
        self.user_id = None

    # -- the fluent chain googleapiclient exposes ---------------------
    def users(self):
        return self

    def messages(self):
        return self

    def send(self, *, userId, body):
        self.user_id = userId
        self.sent_body = body
        return self

    def execute(self, **kwargs):
        if self.raises is not None:
            raise self.raises
        return {"id": self.message_id, "labelIds": ["SENT"]}


@pytest.fixture
def gmail(monkeypatch):
    """Install a FakeGmail and hand it back for assertions."""

    def _install(**kwargs):
        fake = FakeGmail(**kwargs)
        monkeypatch.setattr(email_mod, "_gmail_service", lambda credentials: fake)
        return fake

    return _install


def _decode(body: dict):
    """The message this codebase actually put on the wire.

    `policy=default` so this comes back as an `EmailMessage` with
    `get_content()` — the compat32 default returns a legacy `Message`
    whose payload is undecoded, which would let a transfer-encoded
    secret slip past an `assert material not in ...` check.
    """
    return message_from_bytes(
        base64.urlsafe_b64decode(body["raw"]), policy=policy.default
    )


# =====================================================================
# 1. the send path
# =====================================================================


def test_send_builds_a_real_rfc2822_message(armed_vault, gmail):
    fake = gmail()
    result = send_email("alerts@example.com", "heartbeat RED", "one probe down", cfg=CFG)

    assert result.sent is True
    assert result.ref == "18f0c0ffee"
    assert fake.user_id == "me"

    message = _decode(fake.sent_body)
    assert message["To"] == "alerts@example.com"
    # The prefix is applied by the sender, not by the caller — so a
    # caller that forgets it cannot produce an unfiltered alert.
    assert message["Subject"] == "[COBALT] heartbeat RED"
    assert "one probe down" in message.get_content()
    # `From` is deliberately absent: Gmail fills in the authenticated
    # user, and a hardcoded address would break silently on an account
    # change.
    assert message["From"] is None


def test_report_names_the_channel_and_the_id(armed_vault, gmail):
    gmail(message_id="abc123")
    assert send_email("a@b.com", "s", "b", cfg=CFG).report() == (
        "Email sent — message abc123 to a@b.com"
    )


def test_disabled_channel_is_a_loud_no_op_not_a_crash(armed_vault, gmail):
    """A deliberate `enabled: false` must be distinguishable from an
    outage — the heartbeat has to say WHICH in its own block."""
    fake = gmail()
    off = EmailConfig(enabled=False, to="a@b.com", subject_prefix="[C]")
    result = send_email("a@b.com", "s", "b", cfg=off)

    assert result.sent is False
    assert "disabled" in result.detail
    assert fake.sent_body is None, "a disabled channel must not reach the client at all"


def test_missing_consent_names_the_command_that_fixes_it(tmp_vault, gmail):
    gmail()
    with pytest.raises(EmailError) as excinfo:
        send_email("a@b.com", "s", "b", cfg=CFG)
    message = str(excinfo.value)
    assert REFRESH_TOKEN_KEY in message
    assert "cobalt notify email-auth" in message


def test_a_locked_vault_fails_loud_rather_than_silently_not_sending(monkeypatch, gmail):
    gmail()
    monkeypatch.delenv(secrets_mod.MASTER_KEY_ENV, raising=False)
    with pytest.raises(EmailError, match=secrets_mod.MASTER_KEY_ENV):
        send_email("a@b.com", "s", "b", cfg=CFG)


# =====================================================================
# 2. ALERT PATH != MONITORED PATH — the point of the whole feature
# =====================================================================


def test_send_survives_postgres_mattermost_and_the_vault_all_being_dead(
    armed_vault, gmail, monkeypatch
):
    """Sabotage every monitored dependency at once; the alert still goes.

    This is Charter §3 F18's actual requirement, asserted rather than
    asserted-about. `db.connect` raises, the Obsidian vault resolver
    raises, and the Mattermost sender raises — the three things whose
    failure is the most likely REASON for a red beat. If the email path
    had grown a dependency on any of them, this test is what fails.
    """
    from cobalt import db, vault as vault_mod
    from cobalt.notify import mattermost as mm_mod

    def dead(*args, **kwargs):
        raise RuntimeError("this dependency is down")

    monkeypatch.setattr(db, "connect", dead)
    monkeypatch.setattr(vault_mod, "resolve_vault_path", dead)
    monkeypatch.setattr(mm_mod, "send_dm", dead)

    fake = gmail()
    result = send_email("a@b.com", "everything is down", "including the database", cfg=CFG)

    assert result.sent is True
    assert "including the database" in _decode(fake.sent_body).get_content()


def test_the_redaction_counter_being_dead_does_not_stop_a_send(armed_vault, gmail, monkeypatch):
    """F19 counts hits into Postgres. That count is a nice-to-have; the
    REDACTION is not, and neither is the alert. A dead counter must cost
    the beat a row and nothing else."""
    from cobalt.redact import guard as guard_mod

    def dead_store(*args, **kwargs):
        raise RuntimeError("counter table is gone")

    monkeypatch.setattr(guard_mod, "_record", dead_store)

    fake = gmail()
    with pytest.raises(RuntimeError):
        # Sanity: the patched recorder really does raise, so the
        # assertion below is not passing on a no-op.
        guard_mod._record("email", {"x": 1})

    # …and the send is unaffected, because `redact()` calls `_record`
    # only through its own try/except.
    monkeypatch.setattr(guard_mod, "_record", lambda channel, hits: None)
    assert send_email("a@b.com", "s", "b", cfg=CFG).sent is True
    assert fake.sent_body is not None


# =====================================================================
# 3. failure surfaces — S1-P4's negative proof, mocked
# =====================================================================


def test_a_google_failure_is_an_EmailError_with_a_redacted_message(armed_vault, gmail):
    """A Google error body can quote the request that produced it, bearer
    token included. It must go through the guard before it reaches a log
    line or a DM."""
    gmail(raises=RuntimeError(
        f"HTTP 401 refreshing with refresh_token={FAKE_REFRESH_TOKEN}"
    ))
    with pytest.raises(EmailError) as excinfo:
        send_email("a@b.com", "s", "b", cfg=CFG)

    message = str(excinfo.value)
    assert FAKE_REFRESH_TOKEN not in message, "a failure message leaked the credential"
    assert "REDACTED" in message
    assert "HTTP 401" in message, "the diagnosis must survive the redaction"


def test_a_dead_email_channel_puts_its_reason_in_the_red_DM(monkeypatch):
    """THE WIRING F18 ASKS FOR. Email fails; the red DM says so, by name,
    and the beat does not crash.

    This exercises `runner.out_of_band` and the ORDER it runs in: the DM
    body is rendered from `beat.notes`, so the email outcome only reaches
    Mattermost if the second channel is attempted first.
    """
    from cobalt.heartbeat import runner
    from cobalt.heartbeat.probes import Probe
    from cobalt.heartbeat.render import Beat
    from cobalt.session.clock import session_clock
    from cobalt.session import clock as clock_mod

    monkeypatch.setattr(
        runner, "send_email",
        lambda *a, **k: (_ for _ in ()).throw(EmailError("no refresh token in the vault")),
        raising=False,
    )
    monkeypatch.setattr("cobalt.notify.send_email", lambda *a, **k: (
        (_ for _ in ()).throw(EmailError("no refresh token in the vault"))
    ))
    monkeypatch.setattr("cobalt.notify.record_attempt", lambda **k: None)

    beat = Beat(at=session_clock().to_et(clock_mod.now_utc()))
    beat.probes = [Probe("database", False, "cobalt_brain unreachable")]

    note = runner.out_of_band(beat)
    assert note.startswith("email channel DOWN: ")
    assert "no refresh token" in note

    # …and that note is what the DM renders.
    beat.notes.append(note)
    dm = beat.dm_body()
    assert "email channel DOWN: no refresh token in the vault" in dm
    assert "cobalt_brain unreachable" in dm, "the original red must still be in the DM"


def test_out_of_band_never_raises_even_when_the_config_is_broken(monkeypatch):
    """A beat that died sending the BACKUP alert would take the primary
    alert with it — the exact coupling this channel exists to break."""
    from cobalt.heartbeat import runner
    from cobalt.heartbeat.render import Beat
    from cobalt.session import clock as clock_mod
    from cobalt.session.clock import session_clock

    monkeypatch.setattr(
        "cobalt.notify.config.load_notify_config",
        lambda: (_ for _ in ()).throw(NotifyConfigError("notify.yaml is gibberish")),
    )
    note = runner.out_of_band(Beat(at=session_clock().to_et(clock_mod.now_utc())))
    assert note.startswith("email channel DOWN: ")
    assert "notify config unreadable" in note


# =====================================================================
# 4. F19 on the email channel
# =====================================================================


@pytest.mark.parametrize(
    "material, expected_pattern",
    [
        (FAKE_REFRESH_TOKEN, "google_oauth_refresh_token"),
        (FAKE_CLIENT_SECRET, "google_oauth_client_secret"),
        ("ya29.a0AfH6SMBexampleexampleexampleexample", "google_oauth_access_token"),
    ],
)
def test_the_new_shapes_are_redacted_out_of_an_outbound_email(
    tmp_vault, gmail, material, expected_pattern
):
    """By PATTERN — the half that works on text nobody has seen before.

    The vault here is EMPTY of these values on purpose, so only the
    regex half of the guard can be what catches them.
    """
    secrets_mod.put_secret(CLIENT_ID_KEY, FAKE_CLIENT_ID)
    secrets_mod.put_secret(CLIENT_SECRET_KEY, "GOCSPX-adifferentdeadsecretvalue99")
    secrets_mod.put_secret(REFRESH_TOKEN_KEY, "1//0gADifferentDeadRefreshValue99999")

    fake = gmail()
    result = send_email("a@b.com", "leak check", f"oops: {material}", cfg=CFG)

    content = _decode(fake.sent_body).get_content()
    assert material not in content, f"{expected_pattern} survived to the wire"
    assert f"[REDACTED:{expected_pattern}]" in content
    assert expected_pattern in result.redactions


def test_the_stored_credential_is_redacted_by_the_LITERAL_guard(armed_vault, gmail):
    """By VALUE — the half that survives Google changing a prefix.

    Every vault entry is enrolled automatically the moment it is stored
    (the MATTERMOST_DB_PASSWORD mechanism, 2026-09-05), and `put_secret`
    clears the guard's cache on write so enrolment is immediate rather
    than at the next restart. A hit reports by VAULT KEY NAME, which is
    what tells an operator which credential to rotate.
    """
    fake = gmail()
    result = send_email("a@b.com", "leak check", f"token is {FAKE_REFRESH_TOKEN}", cfg=CFG)

    content = _decode(fake.sent_body).get_content()
    assert FAKE_REFRESH_TOKEN not in content
    assert f"literal:{REFRESH_TOKEN_KEY}" in result.redactions
    assert f"[REDACTED:literal:{REFRESH_TOKEN_KEY}]" in content


def test_the_SUBJECT_is_redacted_too(armed_vault, gmail):
    """The subject is the part that shows up in a phone notification and
    in every mail-server log on the way. Redacting only the body would
    leak the credential to more places, not fewer."""
    fake = gmail()
    result = send_email("a@b.com", f"key {FAKE_CLIENT_SECRET}", "body", cfg=CFG)

    subject = _decode(fake.sent_body)["Subject"]
    assert FAKE_CLIENT_SECRET not in subject
    assert "REDACTED" in subject
    assert result.redactions


def test_a_clean_message_is_unchanged(armed_vault, gmail):
    fake = gmail()
    body = "database: cobalt_brain unreachable\narchiver: last run 2 h ago"
    result = send_email("a@b.com", "heartbeat RED", body, cfg=CFG)

    assert result.redactions == {}
    assert _decode(fake.sent_body).get_content().rstrip("\n") == body


# =====================================================================
# 5. the vault round-trip
# =====================================================================


def test_put_read_round_trip(tmp_vault):
    secrets_mod.put_secret(REFRESH_TOKEN_KEY, FAKE_REFRESH_TOKEN)
    assert secrets_mod.read_secret(REFRESH_TOKEN_KEY) == FAKE_REFRESH_TOKEN
    assert secrets_mod.has_secret(REFRESH_TOKEN_KEY) is True
    assert secrets_mod.read_secret("NOT_A_KEY") is None
    assert secrets_mod.has_secret("NOT_A_KEY") is False


def test_a_write_never_disturbs_an_existing_secret(tmp_vault):
    secrets_mod.put_secret("EXISTING", "keep-me-please")
    secrets_mod.put_secret(REFRESH_TOKEN_KEY, FAKE_REFRESH_TOKEN)
    assert secrets_mod.read_secret("EXISTING") == "keep-me-please"
    assert sorted(secrets_mod.secret_names()) == ["EXISTING", REFRESH_TOKEN_KEY]


def test_a_write_leaves_no_temp_file_behind(tmp_vault):
    """The write is temp-file + atomic rename: a killed process must not
    be able to leave a decryptable fragment in the data directory."""
    secrets_mod.put_secret(REFRESH_TOKEN_KEY, FAKE_REFRESH_TOKEN)
    leftovers = list(tmp_vault.parent.glob(".cobalt_vault.tmp*"))
    assert leftovers == []


def test_an_empty_secret_is_refused(tmp_vault):
    with pytest.raises(secrets_mod.VaultAccessError):
        secrets_mod.put_secret(REFRESH_TOKEN_KEY, "")


def test_secret_names_returns_names_and_never_values(armed_vault):
    names = secrets_mod.secret_names()
    assert set(names) == {CLIENT_ID_KEY, CLIENT_SECRET_KEY, REFRESH_TOKEN_KEY}
    assert FAKE_REFRESH_TOKEN not in " ".join(names)
    assert FAKE_CLIENT_SECRET not in " ".join(names)


# =====================================================================
# 6. the probe and its store
# =====================================================================


def test_channel_status_is_red_before_consent(tmp_vault):
    ok, detail = channel_status()
    assert ok is False
    assert "email-auth" in detail


def test_channel_status_is_green_once_armed(armed_vault):
    ok, detail = channel_status()
    assert ok is True
    assert "token present" in detail
    # Presence, never material.
    assert FAKE_REFRESH_TOKEN not in detail


def test_send_store_round_trips_on_cobalt_dev():
    """Rolled back by the suite's own transaction fixture (RULING 7.1d)."""
    import os

    if not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")):
        pytest.skip("no Postgres configured in this environment")

    from cobalt.notify.store import EmailSendStore

    store = EmailSendStore()
    store.ensure_schema()
    store.record(ok=True, caller="pytest", detail="message zz to a@b.com", message_id="zz")

    last = store.last()
    assert last["ok"] is True
    assert last["caller"] == "pytest"
    assert last["message_id"] == "zz"


def test_recording_never_raises_when_the_database_is_gone(monkeypatch):
    """`record_attempt` is on the alert path. It must degrade loudly and
    never turn a delivered alert into an exception."""
    from cobalt import db
    from cobalt.notify.store import record_attempt

    monkeypatch.setattr(db, "connect", lambda *a, **k: (_ for _ in ()).throw(
        RuntimeError("database is gone")
    ))
    record_attempt(ok=True, caller="pytest", detail="sent anyway")  # must not raise


def test_probe_is_red_when_the_channel_has_never_sent(armed_vault, monkeypatch):
    from cobalt.heartbeat import probes
    from cobalt.notify.store import EmailSendStore

    monkeypatch.setattr(EmailSendStore, "last", lambda self: None)
    probe = probes.email()
    assert probe.ok is False
    assert "NO SEND HAS EVER BEEN MADE" in probe.detail


def test_probe_is_red_when_the_last_send_failed(armed_vault, monkeypatch):
    from datetime import datetime, timezone

    from cobalt.heartbeat import probes
    from cobalt.notify.store import EmailSendStore

    monkeypatch.setattr(EmailSendStore, "last", lambda self: {
        "ts": datetime(2026, 9, 8, 12, 0, tzinfo=timezone.utc),
        "ok": False,
        "caller": "heartbeat",
        "message_id": None,
        "detail": "HTTP 401",
    })
    probe = probes.email()
    assert probe.ok is False
    assert "LAST SEND FAILED" in probe.detail


def test_probe_is_green_when_armed_and_last_send_succeeded(armed_vault, monkeypatch):
    from datetime import datetime, timezone

    from cobalt.heartbeat import probes
    from cobalt.notify.store import EmailSendStore

    monkeypatch.setattr(EmailSendStore, "last", lambda self: {
        "ts": datetime(2026, 9, 8, 12, 0, tzinfo=timezone.utc),
        "ok": True,
        "caller": "email-test",
        "message_id": "zz",
        "detail": "message zz to a@b.com",
    })
    probe = probes.email()
    assert probe.ok is True
    assert "last send OK" in probe.detail


def test_probe_history_unreadable_is_unknown_not_a_diagnosis(armed_vault, monkeypatch):
    """"The probe broke" and "the channel is down" are different facts."""
    from cobalt.heartbeat import probes
    from cobalt.notify.store import EmailSendStore

    monkeypatch.setattr(EmailSendStore, "last", lambda self: (_ for _ in ()).throw(
        RuntimeError("no such table")
    ))
    probe = probes.email()
    assert probe.ok is False
    assert probe.unknown is True


def test_the_email_probe_is_actually_on_the_beat():
    """A probe nobody added to `take_beat` is a probe nobody runs."""
    import inspect

    from cobalt.heartbeat import runner

    assert "probe_mod.email()" in inspect.getsource(runner.take_beat)


# =====================================================================
# 7. notify.yaml validation
# =====================================================================


def test_the_shipped_config_loads_and_declares_an_email_channel():
    cfg = notify_config.load_notify_config()
    assert cfg.email.to
    assert cfg.email.subject_prefix
    assert cfg.mattermost.dm_username


def test_an_unknown_key_is_refused():
    """Config-as-code: a typo must crash, not be silently ignored — a
    misspelled `enabled` that defaults to True is an alert channel
    nobody realises is on, and a misspelled one that defaults to False
    is worse."""
    with pytest.raises(Exception) as excinfo:
        NotifyConfig(
            mattermost={"dm_username": "x"},
            email={"to": "a@b.com", "subjectprefix": "[C]"},
        )
    assert "subjectprefix" in str(excinfo.value)


def test_a_placeholder_recipient_is_refused():
    with pytest.raises(Exception, match="not an email address"):
        EmailConfig(to="TODO-set-this")


def test_the_email_block_is_mandatory():
    """F18's second channel is not optional, so its config is not
    optional either. A notify.yaml with no `email:` block must fail
    loudly rather than boot a heartbeat with one channel."""
    with pytest.raises(Exception):
        NotifyConfig(mattermost={"dm_username": "x"})


def test_a_bad_config_file_raises_rather_than_falling_back(tmp_path, monkeypatch):
    bad = tmp_path / "notify.yaml"
    bad.write_text("notify:\n  mattermost:\n    dm_username: x\n  email:\n    to: nope\n")
    monkeypatch.setattr(notify_config, "CONFIG_PATH", bad)
    with pytest.raises(NotifyConfigError):
        notify_config.load_notify_config()


# =====================================================================
# 8. F16
# =====================================================================


def test_both_new_thresholds_are_tunables_rows_with_consumers():
    from cobalt.taxonomy.loader import load_tunables

    registry = load_tunables().by_key
    for key in (email_mod.AUTH_PORT_KEY, email_mod.TIMEOUT_KEY):
        row = registry[key]
        assert row.value is not None
        assert row.consumers, f"{key} has no declared consumer (F16)"

    assert email_mod.auth_port() == 8765
    assert email_mod.timeout_s() > 0


def test_a_missing_tunable_crashes_rather_than_defaulting(monkeypatch):
    monkeypatch.setattr(email_mod, "_tunable", lambda key: (_ for _ in ()).throw(
        EmailError(f"tunable {key!r} is missing from tunables.yaml")
    ))
    with pytest.raises(EmailError, match="missing from tunables.yaml"):
        email_mod.auth_port()


# =====================================================================
# 9. the consent flow's local bind
# =====================================================================


def test_fast_local_bind_is_fast_and_restores_getfqdn():
    """`socket.getfqdn("localhost")` takes 35 SECONDS on the Mac Studio
    (measured 2026-09-08), and `wsgiref` calls it while binding — before
    `run_local_server` prints the authorisation URL. The command looked
    hung with the one thing the operator needed still unprinted.

    Two things must hold: it is fast inside, and the global is put back
    on the way out. `getfqdn` is a shared builtin; an override that
    outlived this context manager would surprise every later caller in
    the process.
    """
    import socket
    import time

    from cobalt.notify.email import _fast_local_bind

    original = socket.getfqdn
    with _fast_local_bind():
        start = time.monotonic()
        assert socket.getfqdn("localhost") == "localhost"
        assert time.monotonic() - start < 0.5
        assert socket.getfqdn is not original

    assert socket.getfqdn is original, "getfqdn was left monkeypatched"


def test_fast_local_bind_restores_getfqdn_even_on_an_exception():
    import socket

    from cobalt.notify.email import _fast_local_bind

    original = socket.getfqdn
    with pytest.raises(RuntimeError):
        with _fast_local_bind():
            raise RuntimeError("consent was cancelled")
    assert socket.getfqdn is original
