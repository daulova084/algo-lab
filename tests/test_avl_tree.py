import math
import random

import pytest

from algo import AVLTree


def test_insert_and_contains():
    t = AVLTree()
    assert t.insert(5) is True
    assert t.insert(5) is False  # дубликат
    assert 5 in t
    assert 6 not in t
    assert len(t) == 1


def test_sorted_iteration():
    t = AVLTree([5, 1, 9, 3, 7])
    assert list(t) == [1, 3, 5, 7, 9]


def test_min_max():
    t = AVLTree([4, 2, 8])
    assert t.min() == 2
    assert t.max() == 8
    with pytest.raises(ValueError):
        AVLTree().min()
    with pytest.raises(ValueError):
        AVLTree().max()


@pytest.mark.parametrize("keys", [
    list(range(1, 8)),             # LL / RR повороты
    list(range(7, 0, -1)),
    [3, 1, 2],                     # LR
    [1, 3, 2],                     # RL
])
def test_rotations_keep_balance(keys):
    t = AVLTree(keys)
    assert t.is_balanced()
    assert list(t) == sorted(keys)


def test_sequential_insert_height_is_logarithmic():
    n = 1023
    t = AVLTree(range(n))
    assert t.is_balanced()
    assert t.height <= 1.45 * math.log2(n + 2)


def test_delete_cases():
    t = AVLTree(range(1, 16))
    assert t.delete(1) is True      # лист
    assert t.delete(8) is True      # корень с двумя детьми
    assert t.delete(100) is False   # нет такого ключа
    assert 8 not in t and 1 not in t
    assert len(t) == 13
    assert t.is_balanced()
    assert list(t) == [k for k in range(1, 16) if k not in (1, 8)]


def test_random_operations_against_set():
    rng = random.Random(42)
    t = AVLTree()
    ref = set()
    for _ in range(2000):
        k = rng.randint(0, 200)
        if rng.random() < 0.6:
            assert t.insert(k) == (k not in ref)
            ref.add(k)
        else:
            assert t.delete(k) == (k in ref)
            ref.discard(k)
        assert len(t) == len(ref)
    assert list(t) == sorted(ref)
    assert t.is_balanced()
