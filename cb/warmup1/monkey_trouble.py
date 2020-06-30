def monkey_trouble(a_smile, b_smile):
    return a_smile == b_smile


def test_monkey_trouble():
    assert monkey_trouble(True, True) is True
    assert monkey_trouble(False, False) is True
    assert monkey_trouble(True, False) is False
    assert monkey_trouble(False, True) is False


test_monkey_trouble()
