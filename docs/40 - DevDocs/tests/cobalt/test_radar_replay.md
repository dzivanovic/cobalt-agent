# `tests/cobalt/test_radar_replay.py`

Checks replay RVOL synthesis and fail-loud rejection of unsupported fixture filter codes. Its O3 acceptance harness generates bars in-test, converts them to replay snapshots, and drives the replay scan from 04:00 through 20:30 ET with fake stores and a fake session clock. It asserts entry/leave activity, the fixture window and source precedence, both rank-metric boundaries, stickiness retention and expiry, all `ExcludedBy` values through fixture `model_copy` variants, and zero Finviz transport use in overnight and market reset.
