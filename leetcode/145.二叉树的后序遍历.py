# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        print(root.val)

    def postorderTraversal_iter(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res, stack, prev = [], [], None
        stack.append(root)
        while stack or root:
            while root:
                stack.append(root.left)
                root = root.left
            root = stack.pop()
            if not root.right or root.right == prev:
                res.append(root.val)
                prev = root
                root = None
            else:
                stack.append(root)
                root = root.right
                # prev = root
        return res

if __name__ == '__main__':
    s = Solution()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t6 = TreeNode(6)
    t7 = TreeNode(7)
    t1.left = t2
    t2.left = t3
    t2.right = t4
    t1.right = t5
    t5.left = t6
    t6.left = t7

    s.postorderTraversal(t1)
    print(s.postorderTraversal_iter(t1))
