import copy


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        nums = []
        for i in range(1, n + 1):
            nums.append(i)
        res = []
        stack = []
        self.backtrace(nums, 0, k, stack, res)
        return res

    def backtrace(self, nums, start, k, stack, res):
        if len(stack) == k:
            res.append(copy.deepcopy(stack))
            return
        for i in range(start, len(nums)):
            stack.append(nums[i])
            self.backtrace(nums, i + 1, k, stack, res)
            stack.pop()


if __name__ == '__main__':
    s = Solution()
    print(s.combine(4, 2))
