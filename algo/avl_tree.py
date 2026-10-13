class _Node:
    __slots__ = ("key", "left", "right", "height")

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


def _height(node):
    return node.height if node else 0


def _update(node):
    node.height = 1 + max(_height(node.left), _height(node.right))


def _balance(node):
    return _height(node.left) - _height(node.right)


def _rotate_right(y):
    x = y.left
    y.left = x.right
    x.right = y
    _update(y)
    _update(x)
    return x


def _rotate_left(x):
    y = x.right
    x.right = y.left
    y.left = x
    _update(x)
    _update(y)
    return y


def _rebalance(node):
    _update(node)
    b = _balance(node)
    if b > 1:
        if _balance(node.left) < 0:
            node.left = _rotate_left(node.left)
        return _rotate_right(node)
    if b < -1:
        if _balance(node.right) > 0:
            node.right = _rotate_right(node.right)
        return _rotate_left(node)
    return node


class AVLTree:
    """АВЛ-дерево: самобалансирующееся множество ключей (без дубликатов)."""

    def __init__(self, items=()):
        self._root = None
        self._size = 0
        for item in items:
            self.insert(item)

    def __len__(self):
        return self._size

    def __contains__(self, key):
        node = self._root
        while node:
            if key == node.key:
                return True
            node = node.left if key < node.key else node.right
        return False

    def __iter__(self):
        """Ключи в порядке возрастания (итеративный in-order обход)."""
        stack = []
        node = self._root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            yield node.key
            node = node.right

    @property
    def height(self):
        return _height(self._root)

    def insert(self, key):
        """Добавляет ключ. Возвращает True, если ключ новый."""
        self._added = False
        self._root = self._insert(self._root, key)
        if self._added:
            self._size += 1
        return self._added

    def _insert(self, node, key):
        if node is None:
            self._added = True
            return _Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node
        return _rebalance(node)

    def delete(self, key):
        """Удаляет ключ. Возвращает True, если ключ был найден."""
        self._removed = False
        self._root = self._delete(self._root, key)
        if self._removed:
            self._size -= 1
        return self._removed

    def _delete(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            self._removed = True
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            successor = node.right
            while successor.left:
                successor = successor.left
            node.key = successor.key
            # удаляем преемника из правого поддерева, не трогая счётчик
            removed_flag = self._removed
            node.right = self._delete(node.right, successor.key)
            self._removed = removed_flag
        return _rebalance(node)

    def min(self):
        if self._root is None:
            raise ValueError("tree is empty")
        node = self._root
        while node.left:
            node = node.left
        return node.key

    def max(self):
        if self._root is None:
            raise ValueError("tree is empty")
        node = self._root
        while node.right:
            node = node.right
        return node.key

    def is_balanced(self):
        """Проверка инварианта АВЛ (для тестов)."""

        def check(node):
            if node is None:
                return 0
            lh = check(node.left)
            rh = check(node.right)
            if lh < 0 or rh < 0 or abs(lh - rh) > 1:
                return -1
            return 1 + max(lh, rh)

        return check(self._root) >= 0
