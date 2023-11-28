# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from typing import Optional


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        p1 = head
        p2 = head.next
        if p1 == p2:
            return True
        while p1 and p2 and p2.next:  # p2和p2.next都不能为空，判断p2就可以，因为快的不为空，慢的肯定不为空
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:  # 前提一定能相遇，可以与while调换
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    s.hasCycle()
