# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return root

        self.flatten(root.left)
        self.flatten(root.right)

        # 取出左右节点
        left = root.left
        right = root.right

        # 将左置为None， 将左拼到右
        root.left = None
        root.right = left

        # 遍历右最尾端，将左加到右
        p = root
        while p.right:
            p = p.right
        p.right = right


if __name__ == '__main__':
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n6 = TreeNode(6)
    n2 = TreeNode(2, n3, n4)
    n5 = TreeNode(5, None, n6)
    n1 = TreeNode(1, n2, n5)
    s = Solution()
    s.flatten(n1)
