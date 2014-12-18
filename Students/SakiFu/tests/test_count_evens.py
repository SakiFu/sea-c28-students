

from count_evens import count_evens


def test_count_evens():
    assert count_evens([2, 1, 2, 3, 4]) == 3
    assert count_evens([2, 2, 0]) == 3
    assert count_evens([1, 3, 5]) == 0
    assert count_evens([1, 2, 3, 4, 5, 6]) == 2
    assert count_evens([6, 5, 4, 3, 2, 1]) == 3
    assert count_evens([2, 2, 2]) == 3
    assert count_evens([4, 3, 5]) == 1
    assert count_evens([12, 13, 14]) == 2
    assert count_evens([54, 33, 5, 78, 4]) == 3
    assert count_evens([1, 31, 5, 7, 9, 77, 31, 55]) == 0
