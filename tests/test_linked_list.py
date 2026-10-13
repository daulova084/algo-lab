import pytest

from algo import LinkedList


def test_empty():
    lst = LinkedList()
    assert len(lst) == 0
    assert list(lst) == []


def test_append_and_prepend():
    lst = LinkedList([2, 3])
    lst.append(4)
    lst.prepend(1)
    assert list(lst) == [1, 2, 3, 4]
    assert len(lst) == 4


def test_insert_positions():
    lst = LinkedList([1, 3])
    lst.insert(1, 2)
    lst.insert(0, 0)
    lst.insert(len(lst), 4)
    assert list(lst) == [0, 1, 2, 3, 4]
    with pytest.raises(IndexError):
        lst.insert(10, 99)


def test_get_set_item():
    lst = LinkedList([10, 20, 30])
    assert lst[1] == 20
    lst[1] = 25
    assert lst[1] == 25
    with pytest.raises(IndexError):
        lst[3]


def test_remove_head_middle_tail():
    lst = LinkedList([1, 2, 3, 4])
    lst.remove(1)
    lst.remove(3)
    lst.remove(4)
    assert list(lst) == [2]
    lst.append(5)  # хвост должен остаться корректным
    assert list(lst) == [2, 5]


def test_remove_missing():
    with pytest.raises(ValueError):
        LinkedList([1]).remove(2)


def test_pop_front():
    lst = LinkedList([1, 2])
    assert lst.pop_front() == 1
    assert lst.pop_front() == 2
    assert len(lst) == 0
    lst.append(3)
    assert list(lst) == [3]
    with pytest.raises(IndexError):
        LinkedList().pop_front()


def test_index_and_contains():
    lst = LinkedList(["a", "b"])
    assert lst.index("b") == 1
    assert "a" in lst
    assert "z" not in lst
    with pytest.raises(ValueError):
        lst.index("z")


def test_reverse():
    lst = LinkedList([1, 2, 3])
    lst.reverse()
    assert list(lst) == [3, 2, 1]
    lst.append(0)
    assert list(lst) == [3, 2, 1, 0]
    empty = LinkedList()
    empty.reverse()
    assert list(empty) == []
