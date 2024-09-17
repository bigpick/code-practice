#!/usr/bin/env python3

# Given the head of a sorted linked list, delete all duplicates such that
# each element appears only once. Return the linked list sorted as well.

from typing import Optional

TEST_CASES = [
    ([1, 1, 2, 3, 3], [1, 2, 3]),
    ([1, 1, 1, 1, 1], [1]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([1, 2, 2, 3, 3, 4, 4, 5, 5], [1, 2, 3, 4, 5]),
    ([], []),
]


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"Node({self.val}) -> {str(self.next)}"


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        last_seen = head.val
        new_ll = ListNode(last_seen)
        curr_node = new_ll
        while head.next is not None:
            head = head.next
            if head.val == last_seen:
                continue

            last_seen = head.val
            curr_node.next = ListNode(head.val)
            curr_node = curr_node.next

        return new_ll


def ll_from_list(l: list[int]):
    if not l:
        return None

    ll = ListNode(l[0])
    curr = ll
    for val in l[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return ll


for test_case in TEST_CASES:
    assert Solution().deleteDuplicates(ll_from_list(test_case[0])) == ll_from_list(test_case[1])
