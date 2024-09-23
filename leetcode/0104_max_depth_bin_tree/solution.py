#!/usr/bin/env python3

# Given the root of a binary tree, return its maximum depth.
#
# A binary tree's maximum depth is the number of nodes along the longest path from the
# root node down to the farthest leaf node.


from typing import Optional

TEST_CASES = [([3, 9, 20, None, None, 15, 7], 3), ([1, None, 2], 2)]


class TreeNode:
    def __init__(
        self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None
    ) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"TreeNode({self.val})"


def print_bin_tree(tree: "TreeNode", level: int = 0, prefix: str = "root") -> None:
    print(f"{level*' '}{prefix:5s}: val={tree.val}")
    if tree.left:
        print_bin_tree(tree.left, level + 1, "left")
    if tree.right:
        print_bin_tree(tree.right, level + 1, "right")


def bin_tree_from_list(tree_list: list[Optional[int]]) -> Optional["TreeNode"]:
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = []

        def find_depth(node: Optional[TreeNode], depth_so_far: int = 0) -> int:
            if node is None:
                return depth_so_far

            ans.append(find_depth(node.left, depth_so_far + 1))
            ans.append(find_depth(node.right, depth_so_far + 1))

            return max(ans)

        return find_depth(root)


for test_case in TEST_CASES:
    Solution().maxDepth(bin_tree_from_list(test_case[0]))

    assert Solution().maxDepth(bin_tree_from_list(test_case[0])) == test_case[1]
