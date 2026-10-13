class Deque:
    """Дек (двусторонняя очередь) на кольцевом буфере."""

    def __init__(self, items=()):
        self._capacity = 4
        self._data = [None] * self._capacity
        self._head = 0
        self._size = 0
        for item in items:
            self.push_back(item)

    def __len__(self):
        return self._size

    def __iter__(self):
        for i in range(self._size):
            yield self._data[(self._head + i) % self._capacity]

    def __repr__(self):
        return f"Deque({list(self)})"

    def is_empty(self):
        return self._size == 0

    def _grow(self):
        new_data = [None] * (self._capacity * 2)
        for i in range(self._size):
            new_data[i] = self._data[(self._head + i) % self._capacity]
        self._data = new_data
        self._capacity *= 2
        self._head = 0

    def push_back(self, value):
        if self._size == self._capacity:
            self._grow()
        self._data[(self._head + self._size) % self._capacity] = value
        self._size += 1

    def push_front(self, value):
        if self._size == self._capacity:
            self._grow()
        self._head = (self._head - 1) % self._capacity
        self._data[self._head] = value
        self._size += 1

    def pop_back(self):
        if self._size == 0:
            raise IndexError("pop from empty deque")
        idx = (self._head + self._size - 1) % self._capacity
        value = self._data[idx]
        self._data[idx] = None
        self._size -= 1
        return value

    def pop_front(self):
        if self._size == 0:
            raise IndexError("pop from empty deque")
        value = self._data[self._head]
        self._data[self._head] = None
        self._head = (self._head + 1) % self._capacity
        self._size -= 1
        return value

    def peek_front(self):
        if self._size == 0:
            raise IndexError("peek from empty deque")
        return self._data[self._head]

    def peek_back(self):
        if self._size == 0:
            raise IndexError("peek from empty deque")
        return self._data[(self._head + self._size - 1) % self._capacity]
