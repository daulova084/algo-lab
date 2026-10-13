# algo-lab

Учебный репозиторий: структуры данных и сортировки на Python.

## Что внутри

| Модуль | Содержимое |
|---|---|
| `algo/linked_list.py` | Односвязный список |
| `algo/dynamic_array.py` | Динамический массив |
| `algo/deque.py` | Дек на кольцевом буфере |
| `algo/avl_tree.py` | АВЛ-дерево |
| `algo/sorting.py` | Пузырьковая и быстрая сортировки |

## Запуск тестов

```bash
pip install -r requirements.txt
pytest -v
```

Тесты также автоматически запускаются в GitHub Actions при каждом push и pull request
(`.github/workflows/tests.yml`).
