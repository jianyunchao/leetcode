# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        dummy = ListNode(next=head)
        p0 = dummy
        pre = None
        cur = p0.next
        while n >= k:
            n -= k

            for _ in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt

            nxt = p0.next  # 额外变量存储

            p0.next.next = cur
            p0.next = pre

            p0 = nxt  # 重新赋值下一次反转

        return dummy.next
