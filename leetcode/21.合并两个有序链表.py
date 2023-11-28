# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(-1)
        p = dummy
        p1 = list1
        p2 = list2

        while p1 and p2:  # 都有值，因为是有序，其中一个为空，把剩下拼接进去即可
            if p1.val > p2.val:
                p.next = p2
                p2 = p2.next
            else:
                p.next = p1
                p1 = p1.next
            p = p.next

        if p1:
            p.next = p1
        if p2:
            p.next = p2

        return dummy.next

    def my_mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        p = ListNode(-1)

        temp = p
        p1 = list1
        p2 = list2

        while p1 or p2:  # 都有值，因为是有序，其中一个为空，把剩下拼接进去即可
            v1 = p1.val if p1 else 1000
            v2 = p2.val if p2 else 1000
            if v1 > v2:
                temp.next = ListNode(v2)
                p2 = p2.next
            else:
                temp.next = ListNode(v1)
                p1 = p1.next
            temp = temp.next

        return p.next


if __name__ == '__main__':
    s = Solution()

    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(4)
    n1.next = n2
    n2.next = n3

    b1 = ListNode(1)
    b2 = ListNode(3)
    b3 = ListNode(4)
    b1.next = b2
    b2.next = b3

    res = s.mergeTwoLists(n1, b1)
    print(res)