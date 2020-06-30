def parrot_trouble(talking, hour):
    return talking and hour < 7 or talking and hour > 20


def test_parrot_trouble():
    assert parrot_trouble(True, 6) is True
    assert parrot_trouble(True, 7) is False
    assert parrot_trouble(False, 6) is False


test_parrot_trouble()
