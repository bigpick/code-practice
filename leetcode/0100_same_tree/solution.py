#!/usr/bin/env python

from __future__ import annotations

from typing import Optional

TESTS_INPUT = [
    ([1, 2, 3], [1, 2, 3], True),
    ([1, 2], [1, None, 2], False),
    ([1, 2, 1], [1, 1, 2], False),
]


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val = val
        self.left = left
        self.right = right


def bin_tree_from_list(tree_list: list[Optional[int]]) -> Optional[TreeNode]:
    if not tree_list:
        return None

    tree = TreeNode(tree_list[0])
    tree_nodes = [tree]

    for idx, val in enumerate(tree_list[1:]):
        if val is None:
            # leaf
            continue

        parent = tree_nodes[idx // 2]
        is_left_node = (idx % 2) == 0
        new_node = TreeNode(val)

        if is_left_node:
            parent.left = new_node
        else:
            parent.right = new_node
        tree_nodes.append(new_node)
    return tree


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Given the roots of two binary trees p and q, write a function
        # to check if they are the same or not.
        #
        # Two binary trees are considered the same if they are
        # structurally identical, and the nodes have the same value.
        if not p and not q:
            return True
        elif (p and not q) or (q and not p) or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) is self.isSameTree(p.right, q.right) is True


for test_case in TESTS_INPUT:
    ans = Solution().isSameTree(TreeNode(test_case[0]), TreeNode(test_case[1]))
    assert ans == test_case[2]
