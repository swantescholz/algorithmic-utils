from typing import Iterable, Generic, TypeVar, Optional

T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, value: Optional[T] = None, left: Optional["Node[T]"] = None, right: Optional["Node[T]"] = None):
        self.value: Optional[T] = value
        self.left: Node = left
        self.right: Node = right

    def __str__(self) -> str:
        return str(self.value)


class LinkedList(Generic[T]):

    def __init__(self):
        self.first: Node[T] = None
        self.last: Node[T] = None
        self._size = 0

    def __len__(self):
        return self._size

    def appendAll(self, new_values: Iterable[T]):
        for new_value in new_values:
            self.append(new_value)

    def appendLeft(self, new_value: T):
        if self.first is None:
            self.first = Node(new_value)
            self.last = self.first
        elif self.last == self.first:
            self.first = Node(new_value, None, self.last)
            self.last.left = self.first
        else:
            new_node = Node(new_value, None, self.first)
            self.first.left = new_node
            self.first = new_node
        self._size += 1

    def append(self, new_value: T):
        if self.first is None:
            self.first = Node(new_value)
            self.last = self.first
        elif self.last == self.first:
            self.last = Node(new_value, self.first, None)
            self.first.right = self.last
        else:
            new_node = Node(new_value, self.last)
            self.last.right = new_node
            self.last = new_node
        self._size += 1

    class _Iter(Generic[T]):
        def __init__(self, first_node: Node[T]):
            self.current_node : Node[T] = first_node

        def __next__(self) -> T:
            if self.current_node is None:
                raise StopIteration  # signals "the end"
            res = self.current_node.value
            self.current_node = self.current_node.right
            return res

    def __iter__(self):
        return LinkedList._Iter(self.first)

    def __str__(self) -> str:
        return "[" + ", ".join(str(it) for it in self) + "]"

    # returns node after removed node, if any
    def removeNode(self, node: Node[T]):
        if node is None:
            return
        res = node.right
        if node.left is not None:
            node.left.right = node.right
        if self.first == node:
            self.first = node.right
        if node.right is not None:
            node.right.left = node.left
        if self.last == node:
            self.last = node.left
        node.left, node.right = None, None
        self._size -= 1
        return res

    def clear(self):
        node = self.first
        while node is not None:
            node.left = None
            right = node.right
            node.right = None
            node = right
        self.__init__()

if __name__ == '__main__':
    a = LinkedList()
    a.append(1)
    a.appendLeft(2)
    a.appendLeft(3)
    a.appendAll([4,5])
    print(a, len(a))
    a.removeNode(a.first)
    print(a, len(a))
    a.removeNode(a.last.left)
    print(a, len(a))