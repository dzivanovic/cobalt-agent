from cobalt.dayopen.models import CheckResult, Overall, Verdict, overall_verdict


def _result(verdict: Verdict) -> CheckResult:
    return CheckResult("C1", "title", verdict, "detail", "raw")


def test_all_pass_is_green():
    assert overall_verdict([_result(Verdict.PASS), _result(Verdict.PASS)]) == Overall.GREEN


def test_one_fail_is_amber():
    assert overall_verdict([_result(Verdict.PASS), _result(Verdict.FAIL)]) == Overall.AMBER


def test_any_error_is_red_even_alongside_a_fail():
    assert overall_verdict([_result(Verdict.FAIL), _result(Verdict.ERROR)]) == Overall.RED


def test_error_outranks_fail_alone():
    assert overall_verdict([_result(Verdict.ERROR)]) == Overall.RED
