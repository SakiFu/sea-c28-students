def fibonacci(n):
    """First two number of series are 1,2.
    After that, return the (n-2)th number and (n-1)th number."""
    if n < 2:
        return n
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


def lucas(n):
    """First two number of series has to be (2,1).
    After that, return the (n-2)th number and (n-1)th number."""
    if n == 0:
        return 2
    if n == 1:
        return 1
    else:
        return lucas(n - 2) + lucas(n - 1)


def sum_series(n, m=0, l=1):
    if n == 0:
        return m
    if n == 1:
        return l
    else:
        return sum_series(n - 2) + sum_series(n - 1)


if __name__ == "__main__":
    """Test if fibonacci and lucas works properly and test
    if sum_series returns fibonucci
    when it has no optional parameter
    and if it returns lucas when the first two numbers are (2,1)
    and if it returns other series
    when the first numbers are other than that"""
    # assert function(input) == expected
    assert fibonacci(0) = 0
    assert fibonacci(1) = 1
    assert fibonacci(2) = 1
    assert fibonacci(3) = 2
    assert fibonacci(4) = 3
    assert fibonacci(5) = 5
    assert fibonacci(6) = 8
    assert fibonacci(7) = 13
    assert lucas(0) = 2
    assert lucas(1) = 1
    assert lucas(2) = 3
    assert lucas(3) = 4
    assert lucas(4) = 7
    assert lucas(5) = 11
    assert lucas(6) = 18
    assert lucas(7) = 29
    assert sum_series(0) = fibonacci(0)
    assert sum_series(1) = fibonacci(1)
    assert sum_series(2) = fibonacci(2)
    assert sum_series(3) = fibonacci(3)
    assert sum_series(4) = fibonacci(4)
    assert sum_series(5) = fibonacci(5)
    assert sum_series(6) = fibonacci(6)
    assert sum_series(7) = fibonacci(7)
    assert sum_series(0, 2, 1) = lucas(0)
    assert sum_series(1, 2, 1) = lucas(1)
    assert sum_series(2, 2, 1) = lucas(2)
    assert sum_series(3, 2, 1) = lucas(3)
    assert sum_series(4, 2, 1) = lucas(4)
    assert sum_series(5, 2, 1) = lucas(5)
    assert sum_series(6, 2, 1) = lucas(6)
    assert sum_series(7, 2, 1) = lucas(7)
    assert sum_series(3, 3, 4) = 7
    assert sum_series(4, 3, 4) = 11
    assert sum_series(4, 3, 4) = 18
    assert sum_series(3, 4, 6) = 10
    
    print ("All Tests Pass")
