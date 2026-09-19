# APPROVAL LIST — deploy 3 (`53-deploy-d3.md`), as approved by Dejan 16:4x ET (`cto-2026-09-19.md` §4 R36)

The launch line carries **51 `Bash(...)` rules**. **41 are byte-identical** to `38-deploy-p4.md`'s line, which he approved as R30 at 14:23 ET and which ran deploy 2 to `P4 DEPLOY DONE 5b58b7b`. **10 are NEW** — these are what R36 adds:

```
Bash(git -C /Users/cobalt/cobalt tag scratch-allow-probe-d3-0919)
Bash(git -C /Users/cobalt/cobalt tag -d scratch-allow-probe-d3-0919)
Bash(git -C /Users/cobalt/cobalt tag pre-d3-0919)
Bash(git -C /Users/cobalt/cobalt tag deploy-2026-09-19c)
Bash(git -C /Users/cobalt/cobalt merge --ff-only stack/deploy3-0919)
Bash(git -C /Users/cobalt/cobalt worktree add -b stack/deploy3-0919 /Users/cobalt/cobalt-wt/stack-deploy3-0919 main)
Bash(git -C /Users/cobalt/cobalt-wt/stack-deploy3-0919 merge --no-edit *)
Bash(git -C /Users/cobalt/cobalt-wt/stack-deploy3-0919 merge --abort)
Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/stack-deploy3-0919/.env)
Bash(rm /Users/cobalt/cobalt-wt/stack-deploy3-0919/.env)
```

**DROPPED from the deploy-2 line (14), each verified absent:**

```
Bash(git -C /Users/cobalt/cobalt tag deploy-2026-09-19b)
Bash(git -C /Users/cobalt/cobalt-wt/s2-p4 rebase main)
Bash(git -C /Users/cobalt/cobalt tag pre-p4-0919)
Bash(git -C /Users/cobalt/cobalt tag scratch-allow-probe-p4-0919)
Bash(git -C /Users/cobalt/cobalt worktree add -b stack/deploy2-0919 /Users/cobalt/cobalt-wt/stack-deploy2-0919 main)
Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/stack-deploy2-0919/.env)
Bash(rm /Users/cobalt/cobalt-wt/stack-deploy2-0919/.env)
Bash(launchctl bootout gui/501/com.cobalt.replay)
Bash(git -C /Users/cobalt/cobalt-wt/stack-deploy2-0919 merge --abort)
Bash(git -C /Users/cobalt/cobalt-wt/stack-deploy2-0919 merge --no-edit *)
Bash(git -C /Users/cobalt/cobalt tag -d scratch-allow-probe-p4-0919)
Bash(launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.replay.plist)
Bash(git -C /Users/cobalt/cobalt merge --ff-only sprint-2/p4)
Bash(git -C /Users/cobalt/cobalt-wt/s2-p4 rebase --abort)
```

Every other flag is identical to the deploy-2 line: `--model claude-opus-5`, **no `--permission-mode` flag at all** (as `02` and `38` both ran), `--disallowedTools "AskUserQuestion" "EnterWorktree"`, `--add-dir /Users/cobalt/Vault --add-dir /Users/cobalt/cobalt-wt`. `push` appears in no rule, in any spelling.