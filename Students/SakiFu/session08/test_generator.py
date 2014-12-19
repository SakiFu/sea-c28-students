
from generator import sum_int, doubler, fibonacci, prime


def test_sum_int():
    s = sum_int()
    assert s.next() == 0
    assert s.next() == 1
    assert s.next() == 3
    assert s.next() == 6
    assert s.next() == 10
    assert s.next() == 15
    assert s.next() == 21
    assert s.next() == 28


def test_doubler():
    d = doubler()
    assert d.next() == 1
    assert d.next() == 2
    assert d.next() == 4
    assert d.next() == 8
    assert d.next() == 16
    assert d.next() == 32
    assert d.next() == 64


def test_fibonacci():
    f = fibonacci()
    assert f.next() == 1
    assert f.next() == 1
    assert f.next() == 2
    assert f.next() == 3
    assert f.next() == 5
    assert f.next() == 8
    assert f.next() == 13


def test_prime():
    p = prime()
    assert p.next() == 2
    assert p.next() == 3
    assert p.next() == 5
    assert p.next() == 7
    assert p.next() == 11
    assert p.next() == 13
    assert p.next() == 17
    assert p.next() == 19
