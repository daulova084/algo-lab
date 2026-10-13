class _Node:
    __slots__ = ("value", "next")

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    """Односвязный список."""

    def __init__(self, items=()):
        self._head = None
        self._tail = None
        self._size = 0
        for item in items:
            self.append(item)

    def __len__(self):
        return self._size

    def __iter__(self):
        node = self._head
        while node:
            yield node.value
            node = node.next

    def __repr__(self):
        return f"LinkedList({list(self)})"

    def append(self, value):
        node = _Node(value)
        if self._tail is None:
            self._head = self._tail = node
        else:
            self._tail.next = node
            self._tail = node
        self._size += 1

    def prepend(self, value):
        node = _Node(value, self._head)
        self._head = node
        if self._tail is None:
            self._tail = node
        self._size += 1

    def insert(self, index, value):
        if index < 0 or index > self._size:
            raise IndexError("index out of range")
        if index == 0:
            self.prepend(value)
            return
        if index == self._size:
            self.append(value)
            return
        prev = self._node_at(index - 1)
        prev.next = _Node(value, prev.next)
        self._size += 1

    def _node_at(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("index out of range")
        node = self._head
        for _ in range(index):
            node = node.next
        return node

    def __getitem__(self, index):
        return self._node_at(index).value

    def __setitem__(self, index, value):
        self._node_at(index).value = value

    def remove(self, value):
        """Удаляет первое вхождение значения. ValueError, если его нет."""
        prev = None
        node = self._head
        while node:
            if node.value == value:
                if prev is None:
                    self._head = node.next
                else:
                    prev.next = node.next
                if node is self._tail:
                    self._tail = prev
                self._size -= 1
                return
            prev, node = node, node.next
        raise ValueError("value not in list")

    def pop_front(self):
        if self._head is None:
            raise IndexError("pop from empty list")
        node = self._head
        self._head = node.next
        if self._head is None:
            self._tail = None
        self._size -= 1
        return node.value

    def index(self, value):
        for i, v in enumerate(self):
            if v == value:
                return i
        raise ValueError("value not in list")

    def __contains__(self, value):
        return any(v == value for v in self)

    def reverse(self):
        prev = None
        node = self._head
        self._tail = self._head
        while node:
            node.next, prev, node = prev, node, node.next
        self._head = prev
