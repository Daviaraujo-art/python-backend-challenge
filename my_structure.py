"""AVL tree for storing unique integers with logarithmic lookup."""

from dataclasses import dataclass


@dataclass
class _Node:
    value: int
    left: "_Node | None" = None
    right: "_Node | None" = None
    height: int = 1


class MyStructure:
    """Self-balancing binary search tree of unique integers."""

    def __init__(self) -> None:
        self._root: _Node | None = None

    @staticmethod
    def _height(node: _Node | None) -> int:
        return node.height if node else 0

    @classmethod
    def _update_height(cls, node: _Node) -> None:
        node.height = 1 + max(cls._height(node.left), cls._height(node.right))

    @classmethod
    def _rotate_right(cls, node: _Node) -> _Node:
        pivot = node.left
        assert pivot is not None
        node.left = pivot.right
        pivot.right = node
        cls._update_height(node)
        cls._update_height(pivot)
        return pivot

    @classmethod
    def _rotate_left(cls, node: _Node) -> _Node:
        pivot = node.right
        assert pivot is not None
        node.right = pivot.left
        pivot.left = node
        cls._update_height(node)
        cls._update_height(pivot)
        return pivot

    @classmethod
    def _insert(cls, node: _Node | None, value: int) -> tuple[_Node, bool]:
        if node is None:
            return _Node(value), True
        if value == node.value:
            return node, False
        if value < node.value:
            node.left, inserted = cls._insert(node.left, value)
        else:
            node.right, inserted = cls._insert(node.right, value)
        if not inserted:
            return node, False
        cls._update_height(node)
        balance = cls._height(node.left) - cls._height(node.right)
        if balance > 1:
            assert node.left is not None
            if value > node.left.value:
                node.left = cls._rotate_left(node.left)
            return cls._rotate_right(node), True
        if balance < -1:
            assert node.right is not None
            if value < node.right.value:
                node.right = cls._rotate_right(node.right)
            return cls._rotate_left(node), True
        return node, True

    def add(self, value: int) -> bool:
        """Insert value; return True if new, False if repeated."""
        self._root, inserted = self._insert(self._root, value)
        return inserted

    def values(self) -> list[int]:
        """Return unique values in ascending order."""
        result: list[int] = []

        def walk(node: _Node | None) -> None:
            if node is None:
                return
            walk(node.left)
            result.append(node.value)
            walk(node.right)

        walk(self._root)
        return result
