from ackerman import ack


def test_ackerman():
    # if m == 0:
    for n in range(0, 5):
        assert ack(0, n) == n + 1
        assert ack(1, n) == n + 2
        assert ack(2, n) == 2 * (n + 1) + 1

    for n in range(1, 5):
        assert ack(3, n) == ack(2, ack(3, n - 1))

    for m in range(1, 5):
        assert ack(m, 0) == ack(m - 1, 1)

    assert ack(-1, -1) == None
    assert ack(-1, -2) == None
