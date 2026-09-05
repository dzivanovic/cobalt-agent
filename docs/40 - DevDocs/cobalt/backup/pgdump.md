# `src/cobalt/backup/pgdump.py`

## What it does
`pg_dump` of one database to one file, wherever the server actually is.

## This host has no `pg_dump`
Postgres runs in the `cobalt_memory` container (docker-compose,
OrbStack). Dumping through `docker exec` is not a workaround — the
client inside that image is the only one on the machine guaranteed to
match the server (16.12 against 16.12). A host binary is *preferred*
when one exists, because a backup that needs Docker running is a backup
with one more thing that can be down; `shutil.which("pg_dump")` decides,
and the log line says which was used.

## The container is named, not discovered
`CONTAINER = "cobalt_memory"`. A second Postgres container can never be
dumped by accident.

## Exit 0 is not proof
`pg_dump` exits 0 on an empty database, and an empty dump is the backup
that looks green and restores nothing. The dump is rejected unless it is
non-zero AND its last 4 KB carry pg_dump's own
`PostgreSQL database dump complete` marker — which is also the check
that catches a truncated write.
