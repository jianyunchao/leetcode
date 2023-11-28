# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from typing import Optional


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        p1 = head
        p2 = head
        # p2 = head.next  # 偷偷跑了一步？
        # if p1 == p2:
        #     return p1
        while p1 and p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                p2 = head
                count = 0
                while p1 != p2:
                    p1 = p1.next
                    p2 = p2.next
                    count += 1
                return count
        return None


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l1.next = l2
    l2.next = l1
    s = Solution()
    print(s.detectCycle(l1))