"""F19 exfiltration guard — Charter §3 F19, SPRINT-LADDER §S1.

"Outbound secret-regex redactor on every channel. Test: a token in a DM
payload is redacted before send."

What this file proves, and the order matters:

1. EVERY pattern in the shipped config fires on its own shape — driven
   off the config itself, so a pattern added without a case here fails
   the suite rather than shipping untested;
2. a clean message comes back byte-identical;
3. a token inside a URL query string is caught (the shape that leaks
   through logged request URLs, and the one Finviz Elite uses);
4. the guard reports WHAT KIND and never the value;
5. it fails CLOSED — a broken config raises instead of passing text
   through.

NO REAL SECRET APPEARS HERE. Every fixture below is a syntactically
valid, semantically dead sample: right prefix, right character class,
right length, wrong everything else.
"""

import pytest

from cobalt import env
from cobalt.redact import redact
from cobalt.redact.config import CONFIG_PATH, RedactConfigError, load_redact_config
from cobalt.redact.guard import LITERAL_PREFIX
from cobalt.redact.secrets import LiteralGuard

#: One live sample per pattern name in the shipped config, as
#: `(text, the exact material that must not survive)`. Fabricated, never
#: real — see the module docstring. The second element is what the
#: assertions check, because several patterns replace only their
#: `secret` group ON PURPOSE and the context around it is meant to
#: survive: a redacted DSN an operator cannot read is a redactor people
#: route around.
SAMPLES = {
    "private_key_block": (
        "-----BEGIN RSA PRIVATE KEY-----\n"
        "MIIEowIBAAKCAQEAxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"
        "-----END RSA PRIVATE KEY-----",
        "MIIEowIBAAKCAQEAxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    ),
    "jwt": (
        "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0NTY3ODkwIn0.aaaaaaaaaaaaaaaaaaaa",
        "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0NTY3ODkwIn0.aaaaaaaaaaaaaaaaaaaa",
    ),
    "aws_access_key_id": ("AKIAIOSFODNN7EXAMPLE", "AKIAIOSFODNN7EXAMPLE"),
    "aws_secret_access_key": (
        "aws_secret_access_key=wJalrXUtnFEMIK7MDENGbPxRfiCYEXAMPLEKEYA",
        "wJalrXUtnFEMIK7MDENGbPxRfiCYEXAMPLEKEYA",
    ),
    "google_oauth_access_token": (
        "ya29.a0AfH6SMBexampleexampleexampleexample",
        "a0AfH6SMBexampleexampleexampleexample",
    ),
    "google_oauth_refresh_token": (
        "1//0gExampleRefreshTokenValueHere123456",
        "0gExampleRefreshTokenValueHere123456",
    ),
    "google_oauth_client_secret": (
        "GOCSPX-exampleclientsecretvalue123",
        "exampleclientsecretvalue123",
    ),
    "google_api_key": ("AIzaSyAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", "SyAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"),
    "google_api_key_current": (
        "AQ.Ab8RN6ExampleExampleExampleExampleExampleExample",
        "Ab8RN6ExampleExampleExampleExampleExampleExample",
    ),
    "openai_style_key": (
        "sk-proj-0000000000000000000000000000",
        "proj-0000000000000000000000000000",
    ),
    "url_query_secret": (
        "https://elite.finviz.com/export.ashx?v=111&t=AAPL&auth=0000aaaa1111bbbb2222",
        "0000aaaa1111bbbb2222",
    ),
    "finviz_token_named": (
        "finviz_api_token: 2222aaaa3333bbbb4444cccc5555dddd6666",
        "2222aaaa3333bbbb4444cccc5555dddd6666",
    ),
    # `Authorization: Bearer` rather than `MATTERMOST_TOKEN=`: the
    # env-assignment row fires first on the latter and swallows the
    # value, which is correct behaviour and useless as a test of THIS
    # row. Both shapes are how the token actually leaves a process.
    "mattermost_token": (
        "Authorization: Bearer abcdefghijklmnopqrstuvwxyz",
        "abcdefghijklmnopqrstuvwxyz",
    ),
    "basic_auth_header": (
        "Authorization: Basic Y29iYWx0OnBhc3N3b3JkAAAA",
        "Y29iYWx0OnBhc3N3b3JkAAAA",
    ),
    "connection_string_password": (
        "postgresql://cobalt:sup3rs3cr3tpw@100.70.206.126:5432/cobalt_brain",
        "sup3rs3cr3tpw",
    ),
    "env_assignment_secret": (
        "export POSTGRES_PASSWORD=notarealpasswordatall",
        "notarealpasswordatall",
    ),
    # Lower-case + colon: `COBALT_MASTER_KEY=…` is caught one row
    # earlier by env_assignment_secret (also correct, also not a test of
    # this row). Asserted from both directions in TestPatternOverlap.
    "fernet_key": (
        "master_key: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa=",
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa=",
    ),
}


@pytest.fixture(autouse=True)
def no_literals(monkeypatch):
    """Pattern tests run with the literal half OFF.

    The vault is present on this host and `COBALT_MASTER_KEY` is in the
    environment the suite loads, so without this the literal guard would
    redact real credentials out of these fixtures — and a test that
    passes because a REAL secret was caught proves nothing about the
    pattern it names. The literal half has its own tests below, against a
    fabricated guard.
    """
    monkeypatch.setattr(
        "cobalt.redact.guard.load_literals",
        lambda *a, **kw: LiteralGuard({}, available=False, reason="test"),
    )


@pytest.fixture(autouse=True)
def no_counter(monkeypatch):
    """Counting opens a database connection; these are unit tests.
    `TestTheCounter` exercises the real path."""
    monkeypatch.setattr("cobalt.redact.guard._record", lambda *a, **kw: None)


# =====================================================================
# 1. Every pattern, driven off the config
# =====================================================================


class TestEveryShippedPattern:
    def test_the_sample_set_covers_every_pattern_in_config(self):
        """A pattern added to redact.yaml with no case here fails HERE,
        rather than shipping untested and never firing."""
        names = [p.name for p in load_redact_config().patterns]
        assert sorted(names) == sorted(SAMPLES), (
            "every pattern in configs/cobalt/redact.yaml needs a sample in "
            "SAMPLES, and every sample needs a pattern"
        )

    @pytest.mark.parametrize("name", sorted(SAMPLES))
    def test_the_pattern_fires_and_the_material_is_gone(self, name):
        text, secret = SAMPLES[name]
        result = redact(text, channel="test")

        assert name in result.hits, f"{name} did not fire on its own shape"
        assert f"[REDACTED:{name}]" in result.text
        assert secret not in result.text, (
            f"{name}: {len(secret)} chars of the secret survived redaction"
        )

    @pytest.mark.parametrize("name", sorted(SAMPLES))
    def test_no_pattern_needs_another_pattern_to_catch_its_shape(self, name):
        """Each row stands on its own. If `jwt` only ever fired because
        `openai_style_key` happened to overlap it, retiring one would
        silently open the other's hole."""
        text, secret = SAMPLES[name]
        cfg = load_redact_config()
        only = cfg.model_copy(update={"patterns": [p for p in cfg.patterns if p.name == name]})
        result = redact(text, channel="test", cfg=only)
        assert result.hits.get(name), f"{name} does not catch its own sample alone"
        assert secret not in result.text


class TestPatternOverlap:
    """Two rows can legitimately match the same text. What matters is
    that the SECRET is gone either way — the attribution is a diagnostic,
    not a guarantee."""

    @pytest.mark.parametrize(
        "text,secret",
        [
            ("COBALT_MASTER_KEY=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa=",
             "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa="),
            ("MATTERMOST_TOKEN=abcdefghijklmnopqrstuvwxyz",
             "abcdefghijklmnopqrstuvwxyz"),
            ("POSTGRES_PASSWORD=notarealpassword", "notarealpassword"),
        ],
    )
    def test_the_env_line_form_is_caught_whichever_row_gets_there_first(self, text, secret):
        result = redact(text, channel="test")
        assert secret not in result.text
        assert not result.clean


# =====================================================================
# 2. A clean message is untouched
# =====================================================================


class TestCleanText:
    @pytest.mark.parametrize(
        "message",
        [
            "Heartbeat GREEN — 8 jobs, archiver fresh (3,164,539 rows), Obsidian up.",
            "card 846: WATCH -> FILLED (card_transitions ids 1148, 1149, 1150)",
            "REFUSED: it is 20:30:00 ET — inside MARKET RESET.",
            "Day mode REDUCED, sizes from the HALF sheet, keys A, B.",
            "",
        ],
    )
    def test_it_comes_back_byte_identical(self, message):
        result = redact(message, channel="test")
        assert result.text == message
        assert result.clean
        assert result.hits == {}

    def test_an_ordinary_url_keeps_all_of_itself(self):
        url = "https://elite.finviz.com/export.ashx?v=111&t=AAPL&screen=synthetic"
        assert redact(url, channel="test").text == url


# =====================================================================
# 3. A token inside a URL query string
# =====================================================================


class TestTokenInsideAQueryString:
    def test_the_value_goes_and_the_endpoint_stays(self):
        url = "https://elite.finviz.com/export.ashx?v=111&t=AAPL&auth=0000aaaa1111bbbb2222"
        result = redact(url, channel="test")

        assert "0000aaaa1111bbbb2222" not in result.text
        assert result.hits == {"url_query_secret": 1}
        # Everything an operator needs to know WHICH call this was
        # survives — a redactor that makes the line undiagnosable is one
        # people route around at 05:15.
        assert "elite.finviz.com/export.ashx" in result.text
        assert "v=111" in result.text and "t=AAPL" in result.text
        assert "auth=[REDACTED:url_query_secret]" in result.text

    def test_it_catches_every_secret_param_in_one_url(self):
        url = "https://x.test/a?token=aaaaaaaaaaaa&safe=keepme&api_key=bbbbbbbbbbbb"
        result = redact(url, channel="test")
        assert result.hits["url_query_secret"] == 2
        assert "safe=keepme" in result.text

    def test_a_dm_payload_is_redacted_before_send(self):
        """Charter §3 F19's own acceptance test, verbatim."""
        dm = (
            "@dejan heartbeat RED — archiver failed. Retry with:\n"
            "curl 'https://elite.finviz.com/export.ashx?v=111&auth=0000aaaa1111bbbb2222'"
        )
        result = redact(dm, channel="mattermost")
        assert "0000aaaa1111bbbb2222" not in result.text
        assert not result.clean


# =====================================================================
# 4. What the guard reports
# =====================================================================


class TestWhatItReports:
    def test_it_names_the_kind_never_the_value(self):
        result = redact(SAMPLES["jwt"][0], channel="test")
        assert result.describe() == "jwt x1"
        assert SAMPLES["jwt"][1] not in result.describe()

    def test_counts_accumulate_per_pattern(self):
        text = "\n".join(
            [SAMPLES["jwt"][0], SAMPLES["jwt"][0], SAMPLES["aws_access_key_id"][0]]
        )
        result = redact(text, channel="test")
        assert result.hits == {"jwt": 2, "aws_access_key_id": 1}
        assert result.total == 3

    def test_it_destructures_as_text_and_hits(self):
        text, hits = redact(SAMPLES["jwt"][0], channel="test")
        assert "[REDACTED:jwt]" in text and hits == {"jwt": 1}


# =====================================================================
# 5. The literal half
# =====================================================================


class TestLiteralGuard:
    def test_a_vault_value_is_matched_literally_and_named_by_its_key(self, monkeypatch):
        """A human password has no shape. This is the half that catches
        the four 08-23 username/password rotations."""
        monkeypatch.setattr(
            "cobalt.redact.guard.load_literals",
            lambda *a, **kw: LiteralGuard(
                {"finviz.com::password": "correct-horse-battery"}, available=True
            ),
        )
        result = redact("logging in with correct-horse-battery now", channel="test")
        assert "correct-horse-battery" not in result.text
        assert result.hits == {f"{LITERAL_PREFIX}finviz.com::password": 1}

    def test_the_longest_value_wins_so_a_substring_cannot_mangle_it(self, monkeypatch):
        monkeypatch.setattr(
            "cobalt.redact.guard.load_literals",
            lambda *a, **kw: LiteralGuard(
                {"short": "secretpw", "long": "secretpwlonger123"}, available=True
            ),
        )
        result = redact("value: secretpwlonger123", channel="test")
        assert result.hits == {f"{LITERAL_PREFIX}long": 1}

    def test_a_locked_vault_is_not_an_error_and_says_so(self, monkeypatch):
        from cobalt.redact import secrets as secrets_mod

        monkeypatch.delenv(secrets_mod.MASTER_KEY_ENV, raising=False)
        secrets_mod.reset_cache()
        guard = secrets_mod.load_literals(8)
        secrets_mod.reset_cache()
        assert not guard.available
        assert len(guard) == 0
        assert secrets_mod.MASTER_KEY_ENV in guard.reason, (
            "'no literals loaded' has to be visible, never assumed"
        )

    def test_the_guard_exposes_names_not_values(self):
        guard = LiteralGuard({"finviz.com::password": "hunter2hunter2"}, available=True)
        assert guard.names == ["finviz.com::password"]
        assert "hunter2hunter2" not in repr(guard.names)


# =====================================================================
# 6. It fails CLOSED
# =====================================================================


class TestFailsClosed:
    def test_a_missing_config_raises_rather_than_passing_text_through(self, monkeypatch):
        monkeypatch.setattr(
            "cobalt.redact.config.CONFIG_PATH", CONFIG_PATH.parent / "no-such-file.yaml"
        )
        with pytest.raises(RedactConfigError):
            redact("anything", channel="test")

    def test_a_regex_that_does_not_compile_is_refused_at_load(self):
        from cobalt.redact.config import RedactConfig

        with pytest.raises(Exception) as excinfo:
            RedactConfig(
                placeholder="[{name}]",
                literal_min_length=8,
                patterns=[{"name": "bad", "regex": "([unclosed", "because": "x"}],
            )
        assert "does not compile" in str(excinfo.value)

    def test_a_placeholder_that_hides_the_kind_is_refused(self):
        from cobalt.redact.config import RedactConfig

        with pytest.raises(Exception, match=r"\{name\}"):
            RedactConfig(
                placeholder="[REDACTED]",
                literal_min_length=8,
                patterns=[{"name": "x", "regex": "a", "because": "x"}],
            )


# =====================================================================
# 7. The counter the heartbeat reads
# =====================================================================

import os  # noqa: E402

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)


@requires_db
@pytest.mark.integration
class TestTheCounter:
    def test_a_hit_is_counted_with_its_channel_and_never_its_value(self, monkeypatch):
        from datetime import timedelta

        from cobalt.redact.store import RedactionStore
        from cobalt.session import clock as clock_mod

        # `undo()` drops the module's no_counter stub — and every OTHER
        # patch on the same monkeypatch instance with it, including the
        # autouse `dev_env` fixture in conftest.py. Without putting those
        # back, `RedactionStore()` resolves its database with COBALT_ENV
        # unset and RULING 7 correctly refuses. Restore what dev_env sets.
        monkeypatch.undo()
        monkeypatch.setenv(env.ENV_VAR, env.DEV)
        monkeypatch.delenv("COBALT_VAULT_PATH", raising=False)
        store = RedactionStore()
        store.ensure_schema()
        since = clock_mod.now_utc() - timedelta(minutes=1)
        before = store.count_since(since)

        redact(SAMPLES["jwt"][0], channel="mattermost")

        assert store.count_since(since) == before + 1
        rows = store.recent(limit=1)
        assert rows[0]["channel"] == "mattermost"
        assert rows[0]["pattern"] == "jwt"
        # The schema has nowhere to put a value, which is the point.
        assert set(rows[0]) == {"id", "ts", "channel", "pattern", "hits"}

    def test_a_counter_failure_never_blocks_the_send(self, monkeypatch):
        """The redaction has already happened by the time the row is
        written. A database that is down loses the count and says so; the
        text still goes out safe."""
        def _boom(*a, **kw):
            raise RuntimeError("database is down")

        monkeypatch.setattr("cobalt.redact.store.RedactionStore.record", _boom)
        monkeypatch.setattr("cobalt.redact.guard._record", __import__(
            "cobalt.redact.guard", fromlist=["_record"]
        )._record)
        result = redact(SAMPLES["jwt"][0], channel="mattermost")
        assert "[REDACTED:jwt]" in result.text


# =====================================================================
# 8. The two defects the S1-P3 proof run found
# =====================================================================


class TestDefectsFoundByTheProofRun:
    """Both of these passed the tests above and failed on real text.
    Kept as named regressions rather than folded into the sample table."""

    def test_an_env_assignment_mid_line_is_caught(self):
        """The row was anchored to `^`. Every test sample put it on its
        own line — the one place it is least likely to appear in a real
        DM, a real log line or a real pasted config dump."""
        line = "  env        export POSTGRES_PASSWORD=notarealpasswordatall"
        result = redact(line, channel="test")
        assert "notarealpasswordatall" not in result.text
        assert result.hits == {"env_assignment_secret": 1}

    @pytest.mark.parametrize(
        "text,expected",
        [
            ("MATTERMOST_TOKEN=abcdefghijklmnopqrstuvwxyz", "mattermost_token"),
            ("finviz_api_token: 2222aaaa3333bbbb4444cccc5555dddd6666", "finviz_token_named"),
            ("postgresql://cobalt:sup3rs3cr3tpw@h:5432/db", "connection_string_password"),
        ],
    )
    def test_one_secret_is_counted_once_by_its_most_specific_row(self, text, expected):
        """Redacting per pattern, over the previous pattern's OUTPUT,
        let a later row match an earlier row's placeholder — safety was
        never at risk, attribution was, and attribution is the whole
        diagnostic value a redaction leaves behind."""
        result = redact(text, channel="test")
        assert result.hits == {expected: 1}
        assert result.total == 1
        assert result.text.count("[REDACTED:") == 1

    def test_a_placeholder_is_never_itself_redacted(self):
        once = redact("MATTERMOST_TOKEN=abcdefghijklmnopqrstuvwxyz", channel="test")
        twice = redact(once.text, channel="test")
        assert twice.text == once.text, "redaction is idempotent"
        assert twice.clean
