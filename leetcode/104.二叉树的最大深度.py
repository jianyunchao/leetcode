# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution(object):
#     """
#     后序遍历
#     """
#     def maxDepth(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         if not root:
#             return 0
#
#         left_depth = self.maxDepth(root.left)
#         right_depth = self.maxDepth(root.right)
#         return max(left_depth, right_depth) + 1
res = 0
depth = 0


class Solution(object):
    """
    前序遍历
    """

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        global res, depth
        depth += 1
        if not root.left and not root.right:
            res = max(depth, res)
        self.maxDepth(root.left)
        self.maxDepth(root.right)
        depth -= 1


if __name__ == '__main__':
    t3 = TreeNode(3)
    t9 = TreeNode(9)
    t20 = TreeNode(20)
    t15 = TreeNode(15)
    t7 = TreeNode(7)
    t8 = TreeNode(8)

    t3.left = t9
    t3.right = t20
    t20.left = t15
    t20.right = t7
    t7.right = t8

    s = Solution()
    res = res if not s.maxDepth(t3) else s.maxDepth(t3)
    print(res)
