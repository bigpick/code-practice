#!/usr/bin/env python3

"""."""

from typing import Optional


class Node:
    def __init__(self, val: int, next: Optional["Node"] = None) -> None:
        self.val = val
        self.next = None

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        s = f"Node({self.val=})"
        if self.next:
            s += f" -> {self.next}"
        return s


class MyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def get(self, index: int) -> int:
        if not self.head:
            return -1

        curr_node = self.head
        while index > 0 and curr_node:
            curr_node = curr_node.next
            index -= 1

        if index != 0 or not curr_node:
            return -1

        return curr_node.val

    def addAtHead(self, val: int) -> None:
        new = Node(val)
        if not self.head:
            self.head = new
            return

        # insert the new node to the left of the current head
        new.next = self.head
        self.head = new

    def addAtTail(self, val: int) -> None:
        new = Node(val)

        if self.head is None:
            # empty list, just add and return
            self.head = new
            return

        # traverse to the end of the list
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next

        curr_node.next = new

    def addAtIndex(self, index: int, val: int) -> None:
        new = Node(val)
        curr_node = self.head
        idx = 0

        if index == 0:
            self.head = new
            new.next = curr_node
            return

        if not curr_node:
            return

        while idx != index - 1 and curr_node:
            curr_node = curr_node.next
            idx += 1

        if not curr_node:
            return

        next_node = curr_node.next
        curr_node.next = new
        new.next = next_node

    def deleteAtIndex(self, index: int) -> None:
        curr_node = self.head
        if not curr_node:
            return

        if index == 0:
            self.head = self.head.next
            return

        while index > 1 and curr_node:
            index -= 1
            curr_node = curr_node.next

        if not curr_node or index != 1 or not curr_node.next:
            return

        curr_node.next = curr_node.next.next

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return str(self.head)


obj = MyLinkedList()
obj.addAtHead(5)
print(obj)
obj.addAtHead(4)
print(obj)
obj.addAtTail(6)
print(obj)
obj.addAtHead(3)
print(obj)
print(obj.get(0))
print(obj.get(1))
print(obj.get(2))
print(obj.get(3))
print(obj.get(4))
obj.addAtIndex(4, 7)
obj.addAtIndex(0, 0)
obj.addAtIndex(2, 0)
print(obj)
obj.deleteAtIndex(0)
print(obj)
obj.deleteAtIndex(0)
print(obj)
obj.deleteAtIndex(4)
print(obj)
obj.addAtTail(10)
print(obj)
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
