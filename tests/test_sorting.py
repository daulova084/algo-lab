import random

import pytest

from algo import bubble_sort, quick_sort

SORTS = [bubble_sort, quick_sort]


@pytest.mark.parametrize("sort", SORTS)
@pytest.mark.parametrize("data", [
    [],
    [1],
    [2, 1],
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [3, 1, 2, 3, 1, 2],
    [7, 7, 7, 7],
    [-3, 0, 5, -10, 2],
    ["b", "c", "a"],
    [2.5, -1.5, 0.0],
])
def test_known_inputs(sort, data):
    assert sort(data) == sorted(data)


@pytest.mark.parametrize("sort", SORTS)
def test_does_not_mutate_input(sort):
    data = [3, 1, 2]
    sort(data)
    assert data == [3, 1, 2]


@pytest.mark.parametrize("sort", SORTS)
def test_random_arrays(sort):
    rng = random.Random(1)
    for _ in range(50):
        data = [rng.randint(-50, 50) for _ in range(rng.randint(0, 60))]
        assert sort(data) == sorted(data)


def test_quick_sort_large_and_adversarial():
    n = 20000
    assert quick_sort(range(n)) == list(range(n))            # уже отсортирован
    assert quick_sort(range(n, 0, -1)) == list(range(1, n + 1))
    assert quick_sort([1] * n) == [1] * n                    # все равны
