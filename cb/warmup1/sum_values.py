def sum_double(a, b):
    if a == b:
        return (a + b) * 2
    else:
        return a + b


def test_sum_double():
    assert sum_double(1, 2) == 3
    assert sum_double(3, 2) == 5
    assert sum_double(2, 2) == 8
    assert sum_double(-2, -2) == -8


test_sum_double()
