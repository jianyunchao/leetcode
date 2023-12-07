# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        right = dummy
        for _ in range(n):
            right = right.next

        left = dummy
        while right.next:  # 结束条件为right.next
            left = left.next
            right = right.next  # 右指针同步前进
        left.next = left.next.next
        return dummy.next
