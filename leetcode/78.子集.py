import copy


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        stack = []
        self.backtrace(nums, 0, stack, res)
        return res

    def backtrace(self, nums, start, stack, res):
        res.append(copy.deepcopy(stack))
        # res.append(stack.copy())

        for i in range(start, len(nums)):
            stack.append(nums[i])
            # self.backtrace(nums, start + 1, stack)  # 错误点：不是start + 1
            self.backtrace(nums, i + 1, stack, res)
            stack.pop()


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3]
    print(s.subsets(nums))
    # [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    # [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
