#!/usr/bin/env python3

# Asked by Google
#
# Medium
#
#     "text": "Good morning! Here's your coding interview problem for today.\n\nThis problem was asked by Google.\n\nGiven a singly linked list and an integer k, remove the kth last element from\nthe list. k is guaranteed to be smaller than the length of the list.\n\nThe list is very long, so making more than one pass is prohibitively expensive.\n\nDo this in constant space and in one pass."


from __future__ import annotations

from random import randint
from typing import Optional, Sequence


class Node:
    def __init__(self, val: int, next: Optional[Node] = None) -> None:
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"Node({self.val})"

    def __repr__(self) -> str:
        return f"Node({self.val}, next={self.next})"


class LinkedList:
    def __init__(self, root: Optional[Node] = None) -> None:
        self.head = root
        self.size = 1 if root else 0

    def add_node(self, node: Node) -> None:
        if not self.head:
            self.head = node
            return

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = node
        self.size += 1

    @staticmethod
    def from_seq(seq: Sequence[int]) -> LinkedList:
        ll = LinkedList()
        for i in seq:
            ll.add_node(Node(i))
        return ll

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        curr = self.head
        if not curr:
            return "LinkedList()"

        s = f"LinkedList({curr}"
        while curr.next is not None:
            s += f" -> {curr.next}"
            curr = curr.next
        return s + ")"


def remove_kth_last(ll: LinkedList, k: int) -> None:
    before_k_node = curr_node = ll.head
    seen = 0

    while seen < k:
        curr_node = curr_node.next
        seen += 1

    while curr_node.next is not None:
        before_k_node = before_k_node.next
        curr_node = curr_node.next

    before_k_node.next = before_k_node.next.next


for ll_size in range(2, 10):
    kth_from_last = randint(1, ll_size - 1)

    ll = LinkedList.from_seq(range(ll_size))
    print(f"====== Removing {kth_from_last}th from last element ==== ")
    print(f"Before: {ll}")
    remove_kth_last(ll, kth_from_last)
    print(f"After: {ll}")

# ====== Removing 1th from last element ====
# Before: LinkedList(Node(0) -> Node(1))
# After: LinkedList(Node(0))
# ====== Removing 1th from last element ====
# Before: LinkedList(Node(0) -> Node(1) -> Node(2))
# After: LinkedList(Node(0) -> Node(1))
# ====== Removing 1th from last element ====
# Before: LinkedList(Node(0) -> Node(1) -> Node(2) -> Node(3))
# After: LinkedList(Node(0) -> Node(1) -> Node(2))
# ====== Removing 3th from last element ====
# Before: LinkedList(Node(0) -> Node(1) -> Node(2) -> Node(3) -> Node(4))
# After: LinkedList(Node(0) -> Node(1) -> Node(3) -> Node(4))
# ====== Removing 4th from last element ====
# Before: LinkedList(Node(0) -> Node(1) -> Node(2) -> Node(3) -> Node(4) -> Node(5))
# After: LinkedList(Node(0) -> Node(1) -> Node(3) -> Node(4) -> Node(5))
# ====== Removing 6th from last element ====
# Before: LinkedList(Node(0) -> Node(1) -> Node(2) -> Node(3) -> Node(4) -> Node(5) -> Node(6))
# After: LinkedList(Node(0) -> Node(2) -> Node(3) -> Node(4) -> Node(5) -> Node(6))
# ====== Removing 3th from last element ====
# Before: LinkedList(Node(0) -> Node(1) -> Node(2) -> Node(3) -> Node(4) -> Node(5) -> Node(6) -> Node(7))
# After: LinkedList(Node(0) -> Node(1) -> Node(2) -> Node(3) -> Node(4) -> Node(6) -> Node(7))
# ====== Removing 3th from last element ====
# Before: LinkedList(Node(0) -> Node(1) -> Node(2) -> Node(3) -> Node(4) -> Node(5) -> Node(6) -> Node(7) -> Node(8))
# After: LinkedList(Node(0) -> Node(1) -> Node(2) -> Node(3) -> Node(4) -> Node(5) -> Node(7) -> Node(8))
