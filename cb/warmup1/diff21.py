def diff21(n):
    if n <= 21:
        return 21 - n
    else:
        return (n - 21) * 2


def test_diff21():
    assert diff21(19) == 2
    assert diff21(10) == 11
    assert diff21(21) == 0
    assert diff21(22) == 2


test_diff21()
