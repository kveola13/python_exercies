def parrot_trouble(talking, hour):
    if talking and hour < 8 or hour > 20:
        return True


def test_parrot_trouble():
    assert parrot_trouble(True, 6) is True
    assert parrot_trouble(True, 7) is False
    assert parrot_trouble(False, 6) is False


test_parrot_trouble()
