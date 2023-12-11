# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def get_right_view(root, depth):
            if not root:
                return 0
            if depth == len(ans):
                ans.append(root.val)
            get_right_view(root.right, depth + 1)
            get_right_view(root.left, depth + 1)

        get_right_view(root, 0)
        return ans
