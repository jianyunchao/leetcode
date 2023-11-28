import heapq


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None
        import heapq
        queue = []
        dummy = ListNode(-1)
        cur = dummy
        # 这里跟上一版不一样，不再是一股脑全部放到堆中
        # 而是只把k个链表的第一个节点放入到堆中
        for i in range(len(lists)):
            head = lists[i]
            if head:
                heapq.heappush(queue, (head.val, head))
        # 之后不断从堆中取出节点，如果这个节点还有下一个节点，
        # 就将下个节点也放入堆中
        while queue:
            _, head = heapq.heappop(queue)
            cur.next = head
            cur = cur.next
            if head.next:
                heapq.heappush(queue, (head.next.val, head.next))
        cur.next = None
        return dummy.next


class mSolution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        p = dummy
        hp = []
        for head in lists:
            if head:
                print(head.val)
                print(head)
                print(hp)
                heapq.heappush(hp, (head.val, head))

        while hp:
            temp = heapq.heappop(hp)[1]
            p.next = temp
            if temp.next:  # next没有值，为None， 插入heapq报错
                heapq.heappush(hp, (temp.next.val, temp.next))
            p = p.next
        return dummy.next


if __name__ == '__main__':
    x1 = ListNode(1)
    x2 = ListNode(4)
    x3 = ListNode(5)
    x1.next = x2
    x2.next = x3

    y1 = ListNode(1)
    y2 = ListNode(3)
    y3 = ListNode(4)
    y1.next = y2
    y2.next = y3

    z1 = ListNode(2)
    z2 = ListNode(6)
    z1.next = z2
    lists = [x1, y1, z1]
    s = Solution()
    res = s.mergeKLists(lists)
    while res:
        print(res.val)
        res = res.next
    # t = []
    # heapq.heappush(t, (1, ListNode(1)))
    # heapq.heappush(t, (1, ListNode(1)))
    # heapq.heappush(t, (2, ListNode(2)))
    # print(heapq.heappop(t))
    # print(heapq.heappop(t))
