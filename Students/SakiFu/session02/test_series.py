
from series import fibonacci, lucas, sum_series


def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    for i in range(2, 30):
        assert fibonacci(i) == fibonacci(i - 2) + fibonacci(i - 1)


def test_lucas():
    assert lucas(0) == 2
    assert lucas(1) == 1
    for i in range(2, 30):
        assert lucas(i) == lucas(i - 2) + lucas(i - 1)


def test_sum_series():
    for i in range(7):
        assert sum_series(i) == fibonacci(i)
        assert sum_series(i, 2, 1) == lucas(i)
