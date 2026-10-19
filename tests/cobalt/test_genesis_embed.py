"""F21 chunk 2, row V5 (card 469; FINAL F-03, F-09, F-14, F-15): `cobalt genesis embed`.

Offline: the store is a fake with the `GenesisStore` embedding methods and the
route call is a fake `embed_sync`, both patched in before `cobalt.cli.main`
runs. The preflight's failure prints `vectors: DEGRADED`, writes nothing and
exits non-zero (F-03); a failed chunk stays NULL and the run exits non-zero
naming the count (F-14); a re-run embeds only the NULL rows. Every body is
constructed (L32).
"""

from __future__ import annotations

import sys
from types import SimpleNamespace

import pytest

from cobalt import modelaccess
from cobalt.genesis import cli as genesis_cli
from cobalt.modelaccess import ModelCallError

DIM = 8
MODEL = "constructed-embed-model"


class FakeStore:
    def __init__(self, rows):
        #: chunk id -> [body, vector]
        self.rows = {i: [body, vec] for i, (body, vec) in rows.items()}
        self.checked: list[int] = []
        self.writes: list[tuple] = []

    def check_embed_dim(self, dim):
        self.checked.append(dim)

    def null_chunks(self):
        return [(i, body) for i, (body, vec) in sorted(self.rows.items()) if vec is None]

    def set_embedding(self, chunk_id, vector, *, model, dim):
        self.writes.append((chunk_id, model, dim))
        self.rows[chunk_id][1] = vector


class FakeEmbed:
    def __init__(self, fail_on=()):
        self.fail_on = set(fail_on)
        self.texts: list[str] = []

    def __call__(self, route, text, *, caller, config=None):
        self.texts.append(text)
        if text in self.fail_on:
            raise ModelCallError("unreachable", route=route, caller=caller, request_id="r-constructed",
                                 detail="ConnectError")
        return SimpleNamespace(route=route, vector=[0.5] * DIM, dim=DIM, model_returned=MODEL)


def _run(monkeypatch, capsys, store, embed) -> tuple[int, str]:
    monkeypatch.setattr(genesis_cli, "GenesisStore", lambda: store)
    monkeypatch.setattr(modelaccess, "embed_sync", embed, raising=False)
    monkeypatch.setattr(sys, "argv", ["cobalt", "genesis", "embed"])
    from cobalt import cli

    with pytest.raises(SystemExit) as e:
        cli.main()
        raise SystemExit(0)
    out = capsys.readouterr()
    return e.value.code, out.out + out.err


def test_no_vector_at_preflight_prints_degraded_and_writes_nothing(monkeypatch, capsys):
    store = FakeStore({1: ("first constructed chunk", None), 2: ("second constructed chunk", None)})
    embed = FakeEmbed(fail_on={"genesis embed preflight: one synthetic sentence, no user text."})
    code, out = _run(monkeypatch, capsys, store, embed)
    assert code != 0, out
    assert "vectors: DEGRADED" in out
    assert store.writes == [] and store.checked == []
    assert len(embed.texts) == 1, "only the preflight was called"


def test_a_failed_chunk_leaves_it_null_and_exits_nonzero(monkeypatch, capsys):
    store = FakeStore({1: ("chunk one", None), 2: ("chunk two", None), 3: ("chunk three", None)})
    code, out = _run(monkeypatch, capsys, store, FakeEmbed(fail_on={"chunk two"}))
    assert "failed 1" in out and "embedded 2" in out, out
    assert code != 0, out
    assert store.rows[2][1] is None
    assert store.rows[1][1] == [0.5] * DIM and store.rows[3][1] == [0.5] * DIM
    assert [w[0] for w in store.writes] == [1, 3]
    assert store.checked == [DIM]


def test_a_rerun_embeds_only_null_rows(monkeypatch, capsys):
    store = FakeStore({1: ("chunk one", [0.25] * DIM), 2: ("chunk two", None), 3: ("chunk three", None)})
    embed = FakeEmbed()
    code, out = _run(monkeypatch, capsys, store, embed)
    assert code == 0, out
    assert embed.texts[1:] == ["chunk two", "chunk three"]
    assert store.rows[1][1] == [0.25] * DIM
    assert [w for w in store.writes] == [(2, MODEL, DIM), (3, MODEL, DIM)]
    assert "embedded 2" in out and "failed 0" in out


def test_an_over_length_chunk_is_not_sent_and_fails_loud(monkeypatch, capsys):
    # 2047 characters: one over the bound (2048-token context less the two
    # special tokens; a WordPiece token covers at least one character).
    long_body, at_bound = "x" * 2047, "y" * 2046
    store = FakeStore({1: ("chunk one", None), 2: (long_body, None), 3: (at_bound, None)})
    embed = FakeEmbed()
    code, out = _run(monkeypatch, capsys, store, embed)
    assert "over-length 1" in out and "embedded 2" in out, out
    assert code != 0, out
    assert long_body not in embed.texts and at_bound in embed.texts
    assert store.rows[2][1] is None and [w[0] for w in store.writes] == [1, 3]
    from cobalt.genesis.embed import MAX_CHUNK_CHARS

    assert MAX_CHUNK_CHARS == 2046
