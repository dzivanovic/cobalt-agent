# DAY-OPEN 2026-09-15
Generated: 2026-09-16 00:20:22 UTC

## C1 com.cobalt.radar launchd
```
gui/501/com.cobalt.radar = {
	active count = 1
	path = /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist
	type = LaunchAgent
	state = running

	program = /Users/cobalt/.local/bin/uv
	arguments = {
		/Users/cobalt/.local/bin/uv
		run
		cobalt
		radar
		run
	}

	working directory = /Users/cobalt/cobalt

	stdout path = /Users/cobalt/cobalt/logs/radar.log
	stderr path = /Users/cobalt/cobalt/logs/radar.err
	inherited environment = {
		SSH_AUTH_SOCK => /private/tmp/com.apple.launchd.TJt1HQFtTf/Listeners
	}

	default environment = {
		PATH => /usr/bin:/bin:/usr/sbin:/sbin
	}

	environment = {
		COBALT_ENV => production
		PATH => /opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Users/cobalt/.local/bin
		COBALT_VAULT_PATH => /Users/cobalt/Vault/Think
		XPC_SERVICE_NAME => com.cobalt.radar
	}

	domain = gui/501 [100012]
	asid = 100012
	minimum runtime = 10
	exit timeout = 5
	runs = 3
	pid = 8355
	immediate reason = semaphore
	forks = 1
	execs = 1
	initialized = 1
	trampolined = 1
	started suspended = 0
	proxy started suspended = 0
	last exit code = 143

	semaphores = {
		successful exit => 0
	}

	spawn type = daemon (3)
	jetsam priority = 40
	jetsam memory limit (active) = (unlimited)
	jetsam memory limit (inactive) = (unlimited)
	jetsamproperties category = daemon
	jetsam thread limit = 32
	cpumon = default
	probabilistic guard malloc policy = {
		activation rate = 1/1000
		sample rate = 1/0
	}

	properties = runatload | inferred program
}

```

## C2 radar_membership rows
```
count	538
id	pool_key	ticker	trade_date	first_seen_at	entered_at	left_at	source	rank_at_entry	last_rank	below_cap_streak	excluded_by	session
807	primary	PMEC	2026-09-15	2026-09-15 08:00:46.071737+00:00	2026-09-15 08:00:46.071737+00:00	2026-09-15 13:40:03.051570+00:00	screen:morning_low_float@a834132de4fa	8		4		premarket
808	primary	THH	2026-09-15	2026-09-15 08:00:46.071737+00:00	2026-09-15 08:00:46.071737+00:00	2026-09-15 13:40:03.051570+00:00	screen:morning_low_float@a834132de4fa	9		4		premarket
811	primary	DKI	2026-09-15	2026-09-15 08:00:46.071737+00:00	2026-09-15 08:00:46.071737+00:00	2026-09-15 13:40:03.051570+00:00	screen:morning_low_float@a834132de4fa	12		4		premarket
805	primary	HTCO	2026-09-15	2026-09-15 08:00:46.071737+00:00	2026-09-15 08:00:46.071737+00:00	2026-09-15 13:40:03.051570+00:00	screen:morning_low_float@a834132de4fa	6		4		premarket
812	primary	VRAX	2026-09-15	2026-09-15 08:00:46.071737+00:00	2026-09-15 08:00:46.071737+00:00	2026-09-15 13:40:03.051570+00:00	screen:morning_low_float@a834132de4fa	13		4		premarket
pool block metric (market_reset): no rank_metric.market_reset in the 'radar.pool' mirror row
```

## C3 radar beat line
```
newest radar probe line: OK   radar                    paused (market_reset)
newest beat header: HEARTBEAT GREEN — 15 job(s), 13 probe(s), nothing red  (2026-09-15 20:16:55 EDT)
--- heartbeat.err tail
2026-09-15 20:16:57.779 | INFO     | cobalt.heartbeat.runner:run_beat:582 - heartbeat: stage VAULT
2026-09-15 20:16:57.783 | WARNING  | cobalt.heartbeat.runner:run_beat:593 - heartbeat: vault unit DEFERRED — session clock resolved market_reset; no vault write was attempted
2026-09-15 20:16:57.787 | INFO     | cobalt.heartbeat.runner:run_beat:597 - heartbeat: stage FINALIZE
2026-09-15 20:16:57.801 | INFO     | cobalt.heartbeat.runner:run_beat:603 - heartbeat: GREEN — 15 job(s), 13 probe(s), nothing red
2026-09-15 20:16:57.882 | INFO     | cobalt.jobs.wrapper:job_run:196 - F17: com.cobalt.heartbeat DONE
```

## C4 session_blocks heartbeat actor
```
count	8
query: SELECT count(*) FROM session_blocks WHERE actor ~ '^vaultwrite:heartbeat:' (regex operator — never LIKE with %, see day-open-2026-09-14.md S4)
```

## C5 archiver last run
```
last row: ['2026-09-15T00:30:03Z', 'full', 'cobalt_brain', '210', '975', '3165340', '0', '23m19s']
--- archiver.err tail
2026-09-14 20:53:23.849 | INFO     | cobalt.archiver.runner:_run_targets:42 - [975/975] ZTO/i5: 1402 rows
2026-09-14 20:53:23.856 | INFO     | cobalt.archiver.runner:run_full:67 - Run complete: 210 tickers, 3165340 rows, 0 failures, 23m19s. Report: /Users/cobalt/cobalt/docs/30 - Design/archiver-runs.md
2026-09-14 20:53:23.872 | INFO     | cobalt.jobs.wrapper:job_run:196 - F17: com.cobalt.archiver DONE
```

## C6 beats since prior evening
```
window: 2026-09-14 20:00 ET .. 2026-09-15 20:20 ET
beats in window: 97
  2026-09-14 20:11:21
  2026-09-14 20:26:26
  2026-09-14 20:41:29
  2026-09-14 20:56:33
  2026-09-14 21:11:36
  2026-09-14 21:26:40
  2026-09-14 21:40:52
  2026-09-14 21:55:55
  2026-09-14 22:10:58
  2026-09-14 22:26:02
  2026-09-14 22:41:06
  2026-09-14 22:56:09
  2026-09-14 23:11:12
  2026-09-14 23:26:16
  2026-09-14 23:41:20
  2026-09-14 23:56:23
  2026-09-15 00:11:27
  2026-09-15 00:26:30
  2026-09-15 00:41:34
  2026-09-15 00:56:37
  2026-09-15 01:11:41
  2026-09-15 01:26:44
  2026-09-15 01:41:47
  2026-09-15 01:56:51
  2026-09-15 02:11:54
  2026-09-15 02:26:58
  2026-09-15 02:42:01
  2026-09-15 02:57:05
  2026-09-15 03:12:08
  2026-09-15 03:27:12
  2026-09-15 03:42:15
  2026-09-15 03:57:19
  2026-09-15 04:12:22
  2026-09-15 04:27:27
  2026-09-15 04:42:31
  2026-09-15 04:57:34
  2026-09-15 05:12:39
  2026-09-15 05:27:42
  2026-09-15 05:42:47
  2026-09-15 05:57:50
  2026-09-15 06:12:55
  2026-09-15 06:27:59
  2026-09-15 06:43:03
  2026-09-15 06:58:07
  2026-09-15 07:13:10
  2026-09-15 07:28:15
  2026-09-15 07:43:19
  2026-09-15 07:58:24
  2026-09-15 08:13:27
  2026-09-15 08:28:31
  2026-09-15 08:43:36
  2026-09-15 08:58:41
  2026-09-15 09:13:46
  2026-09-15 09:28:49
  2026-09-15 09:43:55
  2026-09-15 09:58:58
  2026-09-15 10:14:03
  2026-09-15 10:29:07
  2026-09-15 10:44:11
  2026-09-15 10:59:16
  2026-09-15 11:14:21
  2026-09-15 11:29:25
  2026-09-15 11:44:30
  2026-09-15 11:59:34
  2026-09-15 12:14:39
  2026-09-15 12:29:42
  2026-09-15 12:44:47
  2026-09-15 12:59:50
  2026-09-15 13:14:55
  2026-09-15 13:29:59
  2026-09-15 13:45:04
  2026-09-15 14:00:07
  2026-09-15 14:15:12
  2026-09-15 14:30:16
  2026-09-15 14:45:21
  2026-09-15 15:00:24
  2026-09-15 15:15:29
  2026-09-15 15:30:33
  2026-09-15 15:45:38
  2026-09-15 16:00:42
  2026-09-15 16:15:47
  2026-09-15 16:30:51
  2026-09-15 16:45:55
  2026-09-15 17:00:59
  2026-09-15 17:16:04
  2026-09-15 17:31:08
  2026-09-15 17:46:12
  2026-09-15 18:01:16
  2026-09-15 18:16:21
  2026-09-15 18:31:24
  2026-09-15 18:46:31
  2026-09-15 19:01:34
  2026-09-15 19:16:40
  2026-09-15 19:31:43
  2026-09-15 19:46:48
  2026-09-15 20:01:51
  2026-09-15 20:16:55
max gap (min): 15.1
FAILED lines in window: 0
```

## VERDICT
| id | check | verdict | detail |
|---|---|---|---|
| C1 | com.cobalt.radar launchd | PASS | state=running, pid=8355, last exit code=143 |
| C2 | radar_membership rows | PASS | count=538, first_seen_at 04:00:46 ET (>= session.premarket_open 04:00) |
| C3 | radar beat line | PASS | OK radar: paused (market_reset) |
| C4 | session_blocks heartbeat actor | PASS | count=8 (expected 8) |
| C5 | archiver last run | PASS | last run 2026-09-14, 0 failures |
| C6 | beats since prior evening | PASS | 97 beat(s), max gap 15.1 min, no FAILED lines |

OVERALL: GREEN
