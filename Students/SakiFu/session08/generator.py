#!/usr/bin/env python


def sum_int():
    i = 0
    a = 1
    while True:
        yield i
        i += a
        a += 1


def doubler():
    x = 0
    while True:
        yield 2 ** x
        x += 1


def fibonacci():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


def prime():
    n = 2
    primes = set()
    while True:
        for i in primes:
            if n % i == 0:
                break
        else:
            primes.add(n)
            yield n
        n += 1
