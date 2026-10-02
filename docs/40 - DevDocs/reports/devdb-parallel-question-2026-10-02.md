# Question for the brain — parallel dev databases (2026-10-02, 17:13 ET)

From: CTO desk `15fed5c2`, on Dejan's order (desk §4 R152). Dejan will read your answer and then talk strategy with you directly. No build, launch or survey follows from this file until he and you settle it.

## The question
Today's 14 hub restarts were all `cobalt_dev` lock collisions, not code rework: one with-DB step at a time (~20 min each), so builds and checks ran in single file from ~08:30 to ~16:30. What is the best step forward? Options on the table so far:
- A: a lock wait (queue) in the hub files instead of FAILED + manual CONTINUE — small, still serial.
- B: a per-hub copy of the dev database so hubs run side by side.
Dejan's bound: maybe two or three parallel copies; anything above that he is very skeptical of. The machine also runs a local LLM (large memory and disk), Mattermost, databases and other services, all in Docker containers on the same host — the desk could not see them from the process list and its sizing below ignored them. Weigh memory, disk and container load against the time saved; say what you would measure first and what you recommend.

## The conversation, verbatim

**Desk (17:03 ET), on the day's rework statistics:**
No check needed a second pass today: all ten checks closed on pass 1, six of them fixing what they held in that pass (18 fixes: `11` five, `17` `18` `19` three each, `12` `21` two each). Two builds were sent back once by the judge seat after a 2-of-3 self-check (`13` a missing hook test, `21` a deploy-card defect). The real waste was the shared dev database: 14 build or check sessions failed on the `cobalt_dev` lock held by another, across 11 jobs (`13` three times, `21` twice), each needing a manual CONTINUE; a lock wait in the hub files is on tomorrow's list.

**Dejan:**
"So the biggest issue we ran into today is not the rework of anything. There was much, much less rework going on all around. The biggest issue is that we have a single entry into a dev database and all the failures really are failures to access database while something else is accessing it. That's what I'm getting out of this."

**Desk:**
Yes: all 14 restarts were sessions that could not get the shared dev database while another build or check held it; none was a code failure. The cost was time — each with-DB step holds it about 20 minutes, so the day ran one at a time from about 8:30 to 4:30. A: hubs wait in a queue for the lock instead of failing (small, still serial). B: each hub gets its own copy of the dev database, so builds and checks run side by side (bigger build, removes the bottleneck). Recommendation: B, with A as a stopgap until B is in.

**Dejan:**
"At what point are we running into a significant system resource issue if we have so many copies of dev database running around?"

**Desk:**
It depends mostly on the dev database's size, which I have not measured. A copy is not a second server, only another database inside the same one: it costs disk, a create time, and the memory its own test run uses. The Mac has 96 GB of memory, 28 cores and 446 GB of free disk, and today never ran more than about six hubs at once, so I expect the meter to limit us before the machine does. But I could not see a database server process on this Mac, so it may run elsewhere and that host's limits are the ones that matter. Offered a read-only Sonnet survey of host, size and copy time before he picks A or B.

**Dejan (17:12 ET), his direction:**
"You shouldn't do any of that. The machine runs a local LLM model and it needs a significant amount of memory and space for that. And it has a bunch of other things like Mattermost and databases and other things. And they all run in Docker containers on the same machine. You couldn't see it on the machine because they are in its their own Docker containers. So this is a discussion that needs to be dealt with a little bit more sensitive than what you're thinking. So I want to package a question for the brain with these three last messages in our conversation since I asked you about the rework and a size. And what we need to do is I want to talk to Brain about figuring out what is the best step forward. Maybe we can run two or three parallel copies, but anything above that, I would be very skeptical is a good idea. Uh, send a copy of this to the Brain with question and tell him that I'm gonna look at his output and start talking to him about the strategy of how to move forward."

## Pointers
- Desk report `reports/cto-2026-10-02.md` §4: lock FAILs R61, R62, R69, R80, R86–R91, R100, R101, R115, R122; lock rules R64, R66, R104; CONTINUE order in §5 LOCK QUEUE.
- Machine facts the desk read: `sysctl hw.memsize` 103079215104, `hw.ncpu` 28; `df -h /` 446 Gi free of 926 Gi. Docker container footprints not read.
- Write your answer to `reports/devdb-parallel-answer-2026-10-02.md` and MESSAGE `cto-desk` its path.
