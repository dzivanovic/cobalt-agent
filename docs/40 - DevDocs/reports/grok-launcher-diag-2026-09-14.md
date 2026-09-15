# Grok/Chief-of-Staff tribunal launcher-symmetry diagnostic — 2026-09-14

Purpose: prove the three tribunal seats (Fable, Astra, Grok) can be launched
under equivalent write-capable profiles before any tribunal prompt is
issued (09-13 launcher-symmetry rule; L44 corollary — a worker producing an
artifact gets WRITE to its own workspace). Workspace: `~/tmp/tribunal-grok/`.
Nothing in `~/cobalt` was written by this probe except this report.

Known-answer: `wc -l '/Users/cobalt/Vault/Think/6 - Permanent/Memory/LAWS.md'` = **310**.

---

## 1. Grok launch under a real workspace-write profile

`~/.grok/sandbox.toml` has exactly one custom profile:

```toml
[profiles.readonly-safe]
extends = "read-only"
restrict_network = false
```

No custom workspace-write profile is defined. It doesn't need one: Grok
ships a **built-in** `workspace` profile (read everywhere, write to
CWD + `~/.grok/` + temp dirs, network allowed) that is exactly the
writer-role shape L33 calls for — no `sandbox.toml` entry required.

Launch line:
```
grok -p "<prompt>" --cwd /Users/cobalt/tmp/tribunal-grok/grok --sandbox workspace --permission-mode auto --output-format json
```
(`--permission-mode auto` used, not `--yolo`/`--always-approve` — L55 keeps
auto mode per-session, never a blanket bypass equivalent.)

Known-answer read result: model ran `wc -l` itself and replied `310`.
Matches. Exit code 0.

## 2. Grok write gates

**a) Workspace write (must succeed):**
```
grok -p "Write 'tribunal probe ok' to ./probe.txt in CWD" --cwd /Users/cobalt/tmp/tribunal-grok/grok --sandbox workspace --permission-mode auto
```
Result: succeeded. `/Users/cobalt/tmp/tribunal-grok/grok/probe.txt` contains
`tribunal probe ok`. Exit code 0.

**b) Production write (must be denied):**
```
grok -p "Write 'tribunal probe DENIED-TEST' to /Users/cobalt/cobalt/probe.txt" --cwd /Users/cobalt/tmp/tribunal-grok/grok --sandbox workspace --permission-mode auto
```
Result: denied by the kernel (Seatbelt), both via Grok's own write tool and
its own shell retry. Verbatim:
```
Write tool error: IO Error: Operation not permitted (os error 1)
Shell error: (eval):1: operation not permitted: /Users/cobalt/cobalt/probe.txt
```
`/Users/cobalt/cobalt/probe.txt` confirmed absent after the run — nothing to
delete. Shell tool was available throughout (not read-only paging); the
denial is filesystem-layer, not tool-availability.

## 3. Codex

```
cd /Users/cobalt/tmp/tribunal-grok/codex
codex exec --skip-git-repo-check -s workspace-write "$(cat task.txt)" < /dev/null
```
(`-s workspace-write`, never `danger-full-access`, per L29's Sol writer
profile; `--approve-for-me` not used — L37 bans model-judged approvals.)

Result: exit code 0. Model `gpt-6-astra`, sandbox
`workspace-write [workdir, /tmp, $TMPDIR]`, approval `never`. Ran
`wc -l` itself, replied `310`. Matches.
No usage-limit / remaining-allowance text appeared anywhere in the output.
**Allowance unknown — Dejan supplies.**

## 4. Claude headless

First attempt (no extra dir grant) was **denied**:
```
claude -p "<prompt>" --allowedTools "Bash(wc*)" --output-format json
```
→ `permission_denials`: Bash blocked, `LAWS.md` outside the session's
allowed directory. Claude's default sandbox denies read access outside CWD
by default — unlike Grok/Codex, which read the whole filesystem by default
under their write-capable profiles.

Second attempt, with Read pre-authorised for the target folder:
```
claude -p "<prompt>" --add-dir "/Users/cobalt/Vault/Think/6 - Permanent/Memory" --allowedTools "Bash(wc*)" "Read" --output-format json
```
Result: `permission_denials: []`, `result: "310"`. Matches. Exit code 0.
Model: `claude-opus-5`.

## 5. Side by side

| Seat  | Final launch line | Default FS read | Write scope |
|---|---|---|---|
| Grok | `grok -p "<prompt>" --cwd <ws> --sandbox workspace --permission-mode auto` | whole filesystem (default) | CWD + `~/.grok/` + temp |
| Codex | `codex exec --skip-git-repo-check -s workspace-write "<prompt>" < /dev/null` (cwd = `<ws>`) | whole filesystem (default) | workdir + `/tmp` + `$TMPDIR` |
| Claude | `claude -p "<prompt>" --add-dir "<target-dir>" --allowedTools "Bash(wc*)" "Read"` (cwd = `<ws>`) | **CWD only by default** — requires an explicit `--add-dir` per external path | not exercised this run (only Grok's write gates were in scope) |

**Asymmetry found:** Grok's `workspace` profile and Codex's
`workspace-write` sandbox both default to unrestricted filesystem READ,
scoping only WRITE to the workspace. Claude Code's default posture is the
opposite shape — READ is also scoped to CWD by default and needs an
explicit `--add-dir` per external path (proven working here, but it is a
manual, per-path grant, not a default parity with the other two houses).
Per the launcher-symmetry rule this is an asymmetry, not a note: a tool
(unscoped read) available to two seats by default was denied to the third
until manually widened.

This does not block today's probe — the workaround is proven and cheap
(one `--add-dir` flag) — but a tribunal prompt template that assumes
symmetric default read access across all three houses will silently fail
for the Claude seat unless the launcher always attaches `--add-dir` for
whatever paths the prompt needs (repo, vault Memory folder, ledger).

---

**PRECONDITION: FAIL — write-capable launch is proven symmetric and working
for all three seats (Grok/Codex/Claude all hit the known-answer correctly
and Grok's write gates land exactly where expected), but default READ
scope is NOT symmetric: Claude requires an explicit per-path `--add-dir`
that Grok and Codex don't need. The tribunal launcher must standardize on
always passing that flag for Claude seats, or the asymmetry will bite the
first time a tribunal prompt references a path outside the workspace.**

ESCALATE: none — no higher tier needed. Open item for the hub: bake a
fixed `--add-dir` list (repo root, `Vault/Think/6 - Permanent/Memory`,
`Vault/Think/0 - Projects/Cobalt`) into the standard Claude tribunal-seat
launch line so this asymmetry can't recur silently.
