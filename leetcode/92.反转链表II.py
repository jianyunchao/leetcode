# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy_node = ListNode(next=head)
        # dummy_node.next = head
        p0 = dummy_node
        # while left > 0:  #  操作left导致后面报错
        #     p0 = p0.next
        #     left -= 1
        for _ in range(left - 1):
            p0 = p0.next

        pre = None
        cur = p0.next
        # pre = p0
        # while right - left > 0:
        for _ in range(right - left + 1):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
            right -= 1

        p0.next.next = cur
        p0.next = pre
        return dummy_node.next
