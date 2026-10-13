class DynamicArray:
    """Динамический массив с удвоением ёмкости."""

    def __init__(self, items=()):
        self._capacity = 4
        self._size = 0
        self._data = [None] * self._capacity
        for item in items:
            self.append(item)

    def __len__(self):
        return self._size

    def __iter__(self):
        for i in range(self._size):
            yield self._data[i]

    def __repr__(self):
        return f"DynamicArray({list(self)})"

    @property
    def capacity(self):
        return self._capacity

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity

    def _check(self, index):
        if index < 0:
            index += self._size
        if index < 0 or index >= self._size:
            raise IndexError("index out of range")
        return index

    def __getitem__(self, index):
        return self._data[self._check(index)]

    def __setitem__(self, index, value):
        self._data[self._check(index)] = value

    def append(self, value):
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        self._data[self._size] = value
        self._size += 1

    def insert(self, index, value):
        if index < 0 or index > self._size:
            raise IndexError("index out of range")
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        for i in range(self._size, index, -1):
            self._data[i] = self._data[i - 1]
        self._data[index] = value
        self._size += 1

    def pop(self, index=-1):
        index = self._check(index)
        value = self._data[index]
        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]
        self._size -= 1
        self._data[self._size] = None
        if self._capacity > 4 and self._size <= self._capacity // 4:
            self._resize(self._capacity // 2)
        return value

    def index(self, value):
        for i in range(self._size):
            if self._data[i] == value:
                return i
        raise ValueError("value not in array")

    def __contains__(self, value):
        return any(v == value for v in self)
