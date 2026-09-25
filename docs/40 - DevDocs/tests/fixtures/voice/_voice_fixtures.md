# `tests/fixtures/voice/` — voice V1 fixtures

TEXT only. No audio file is ever committed: test audio is synthesized at
test time (`say` → PyAV) into `tmp_path` (R18 (b), L45 real container,
synthetic content). No value of the trader's (L32).

| file | SHAPE | what it holds |
|---|---|---|
| `plan-replies.constructed.yaml` | `SHAPE: constructed` | hand-written model replies + the transcript and candidate ids each is checked against, with the expected outcome (a Plan kind or the `voice_plan` failure kind) — C3 |
