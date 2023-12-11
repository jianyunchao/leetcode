# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_height(root):
            if not root:
                return 0
            l = get_height(root.left)
            if l == -1:
                return -1
            r = get_height(root.right)
            if r == -1 or abs(l - r) > 1:
                return -1
            return max(l, r) + 1

        return get_height(root) != -1
