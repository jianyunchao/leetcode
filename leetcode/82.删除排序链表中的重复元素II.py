# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        if not dummy.next or not dummy.next.next:
            return dummy.next

        cur = dummy
        while cur.next and cur.next.next:
            val = cur.next.val
            if val == cur.next.next.val:
                while cur.next and cur.next.val == val:
                    cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next
