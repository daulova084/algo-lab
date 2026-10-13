import random


def bubble_sort(items):
    """Пузырьковая сортировка. Возвращает новый отсортированный список."""
    result = list(items)
    n = len(result)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break
    return result


def quick_sort(items):
    """Быстрая сортировка (случайный опорный элемент, трёхстороннее разбиение).
    Возвращает новый отсортированный список."""
    result = list(items)
    _quick_sort(result, 0, len(result) - 1)
    return result


def _quick_sort(a, lo, hi):
    while lo < hi:
        pivot = a[random.randint(lo, hi)]
        lt, i, gt = lo, lo, hi
        while i <= gt:
            if a[i] < pivot:
                a[lt], a[i] = a[i], a[lt]
                lt += 1
                i += 1
            elif a[i] > pivot:
                a[i], a[gt] = a[gt], a[i]
                gt -= 1
            else:
                i += 1
        # рекурсия в меньшую часть, цикл в большую — глубина O(log n)
        if lt - lo < hi - gt:
            _quick_sort(a, lo, lt - 1)
            lo = gt + 1
        else:
            _quick_sort(a, gt + 1, hi)
            hi = lt - 1
