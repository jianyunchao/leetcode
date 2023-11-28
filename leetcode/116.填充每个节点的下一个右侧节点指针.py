import collections


# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return []
        d = collections.deque()
        d.append(root)
        while d:

            limit = len(d)
            for x in range(limit):
                temp = d.popleft()
                if x < limit - 1 and d:
                    temp.next = d[0]
                if temp.left:
                    d.append(temp.left)
                if temp.right:
                    d.append(temp.right)
        return root


if __name__ == '__main__':
    n7 = Node(7, None, None, None)
    n6 = Node(6, None, None, None)
    n5 = Node(5, None, None, None)
    n4 = Node(4, None, None, None)
    n3 = Node(3, n6, n7, None)
    n2 = Node(2, n4, n5, None)
    n1 = Node(1, n2, n3, None)
    s = Solution()
    s.connect(n1)
