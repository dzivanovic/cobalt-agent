"""C1's parser — `launchctl print gui/<uid>/<label>`.

`launchctl_print_running.txt`'s four load-bearing fields (state, runs,
pid, last exit code) are the REAL values captured in
`docs/40 - DevDocs/reports/day-open-2026-09-14.md` S1 (L45); the
surrounding `{ ... }` block is the real `launchctl print` wrapper shape.
`launchctl_print_not_running.txt` is a constructed variant of the same
real field set — capturing a genuinely stopped `com.cobalt.radar` live
would mean stopping production radar, which is out of scope for a test.
"""

from pathlib import Path

from cobalt.dayopen.launchd import parse_launchctl_print

FIXTURES = Path(__file__).resolve().parents[1] / "fixtures" / "dayopen"


def test_running_with_pid():
    text = (FIXTURES / "launchctl_print_running.txt").read_text()
    status = parse_launchctl_print("com.cobalt.radar", text)
    assert status.state == "running"
    assert status.pid == 27385
    assert status.runs == 1
    assert status.last_exit_code == "(never exited)"
    assert status.running_with_pid is True
    assert status.raw == text


def test_not_running_has_no_pid():
    text = (FIXTURES / "launchctl_print_not_running.txt").read_text()
    status = parse_launchctl_print("com.cobalt.radar", text)
    assert status.state == "not running"
    assert status.pid is None
    assert status.runs == 4
    assert status.last_exit_code == "1"
    assert status.running_with_pid is False


def test_empty_output_is_all_none():
    status = parse_launchctl_print("com.cobalt.radar", "")
    assert status.state is None
    assert status.pid is None
    assert status.runs is None
    assert status.running_with_pid is False
