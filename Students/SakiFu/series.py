def fibonacci(n):
    """Return fibonacci function.First two number of series are (0,1), which is n.
    After 2, return the sum of (n-2)th number and (n-1)th number."""

    if n < 2:
        return n
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


def lucas(n):
    """Return lucas function. First two number of series has to be (2,1).
    After that, return the sum of (n-2)th number and (n-1)th number."""

    if n == 0:
        return 2
    if n == 1:
        return 1
    else:
        return lucas(n - 2) + lucas(n - 1)


def sum_series(n, m=0, r=1):
    sum_series(n) == fibonacci(n)
    sum_series(n, 2, 1) == lucas(n)
    return sum_series(n - 2) + sum_series(n - 1)


if __name__ == "__main__":
    """Test if fibonacci, lucas and sum_series work properly.
    Tests if sum_series returns fibonucci
    when it has no optional parameter
    and if it returns lucas when the first two numbers are (2,1)
    and if it returns other series
    when the first numbers are other than that"""
    # assert function(input) == expected
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(2) == 3
    assert lucas(3) == 4
    assert lucas(4) == 7
    assert lucas(5) == 11
    assert lucas(6) == 18
    assert lucas(7) == 29

    for i in range(7):
        assert sum_series(n) == fibonacci(n)
        assert sum_series(n, 2, 1) == lucas(n)
    
    print ("All Tests Pass")

