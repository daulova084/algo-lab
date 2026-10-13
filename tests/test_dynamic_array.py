import pytest

from algo import DynamicArray


def test_append_and_growth():
    arr = DynamicArray()
    for i in range(100):
        arr.append(i)
    assert len(arr) == 100
    assert list(arr) == list(range(100))
    assert arr.capacity >= 100


def test_get_set_negative_index():
    arr = DynamicArray([1, 2, 3])
    assert arr[-1] == 3
    arr[0] = 10
    assert arr[0] == 10
    with pytest.raises(IndexError):
        arr[3]
    with pytest.raises(IndexError):
        arr[-4]


def test_insert():
    arr = DynamicArray([1, 3])
    arr.insert(1, 2)
    arr.insert(0, 0)
    arr.insert(4, 4)
    assert list(arr) == [0, 1, 2, 3, 4]
    with pytest.raises(IndexError):
        arr.insert(10, 1)


def test_pop():
    arr = DynamicArray([1, 2, 3, 4])
    assert arr.pop() == 4
    assert arr.pop(0) == 1
    assert list(arr) == [2, 3]
    with pytest.raises(IndexError):
        DynamicArray().pop()


def test_shrinks_after_many_pops():
    arr = DynamicArray(range(64))
    big = arr.capacity
    for _ in range(60):
        arr.pop()
    assert arr.capacity < big
    assert list(arr) == [0, 1, 2, 3]


def test_index_contains():
    arr = DynamicArray(["x", "y"])
    assert arr.index("y") == 1
    assert "x" in arr
    assert "q" not in arr
    with pytest.raises(ValueError):
        arr.index("q")
