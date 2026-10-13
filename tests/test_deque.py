import pytest

from algo import Deque


def test_push_pop_both_ends():
    d = Deque()
    d.push_back(2)
    d.push_back(3)
    d.push_front(1)
    d.push_front(0)
    assert list(d) == [0, 1, 2, 3]
    assert d.pop_front() == 0
    assert d.pop_back() == 3
    assert list(d) == [1, 2]


def test_peek():
    d = Deque([1, 2, 3])
    assert d.peek_front() == 1
    assert d.peek_back() == 3
    assert len(d) == 3


def test_empty_errors():
    d = Deque()
    assert d.is_empty()
    for op in (d.pop_front, d.pop_back, d.peek_front, d.peek_back):
        with pytest.raises(IndexError):
            op()


def test_wraparound_and_growth():
    d = Deque()
    for i in range(50):
        d.push_front(i)
    assert list(d) == list(range(49, -1, -1))
    for i in range(25):
        assert d.pop_back() == i
    for i in range(100, 130):
        d.push_back(i)
    assert len(d) == 55
    assert d.peek_back() == 129
    assert d.peek_front() == 49


def test_fifo_queue_behavior():
    d = Deque()
    for i in range(10):
        d.push_back(i)
    assert [d.pop_front() for _ in range(10)] == list(range(10))
    assert d.is_empty()
