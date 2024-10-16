#!/usr/bin/env python3

from __future__ import annotations

from typing import Optional

# Given the root of a binary tree, return the inorder traversal of its nodes' values.

TEST_CASES = [
    ([1, None, 2, 3], [1, 3, 2]),
    ([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9], [4, 2, 6, 5, 7, 1, 3, 9, 8]),
    ([], []),
    ([1], [1]),
]


class TreeNode:
    def __init__(
        self, val: int = 0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None
    ):
        self.val = val
        self.left = left
        self.right = right


def print_bin_tree(tree: TreeNode, level: int = 0, prefix: str = "root") -> None:
    print(f"{level * '  '}{prefix:5s}: val={tree.val}")
    if tree.left:
        print_bin_tree(tree.left, level + 1, "left")
    if tree.right:
        print_bin_tree(tree.right, level + 1, "right")


def tree_from_list(root_list: list[int]) -> Optional[TreeNode]:
    if not root_list:
        return None

    root = TreeNode(root_list[0])
    tree_nodes = [root]
    for idx, val in enumerate(root_list[1:]):
        if val is None:
            continue
        parent = tree_nodes[idx // 2]
        is_left_node = idx % 2 == 0
        node = TreeNode(val)
        if is_left_node:
            parent.left = node
        else:
            parent.right = node

        tree_nodes.append(node)

    return root


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        def traverse_tree(node: Optional[TreeNode], seen=None):
            if seen is None:
                seen = []
            if node is None:
                return []

            traverse_tree(node.left)
            seen.append(node.val)
            traverse_tree(node.right)

            return seen

        return traverse_tree(tree_from_list(root))


for test_case in TEST_CASES:
    print(Solution().inorderTraversal(test_case[0]))
    assert Solution().inorderTraversal(test_case[0]) == test_case[1]
