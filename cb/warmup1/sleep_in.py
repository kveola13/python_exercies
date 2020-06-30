def sleep_in(weekday, vacation):
    return vacation or not weekday


def test_sleep_in():
    assert sleep_in(False, False) is True
    assert sleep_in(True, False) is False
    assert sleep_in(False, True) is True
    assert sleep_in(True, True) is True


test_sleep_in()
