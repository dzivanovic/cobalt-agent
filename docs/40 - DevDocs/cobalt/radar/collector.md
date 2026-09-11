# `src/cobalt/radar/collector.py`

Strict Finviz screener collector using the shared transport and one process token bucket. It parses CSV by header name, refuses redirects/HTML/missing headers, chunks ticker lists, and caches raw responses only under gitignored `data/radar-cache`.

