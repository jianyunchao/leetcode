import copy


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        stack = []
        self.dfs(nums, stack, res)
        return res

    def dfs(self, nums, stack, res):
        if len(nums) == len(stack):
            res.append(copy.deepcopy(stack))

        for i in range(len(nums)):  # for循环
            if nums[i] in stack:  # 做选择
                continue
            stack.append(nums[i])
            self.dfs(nums, stack, res)  # 递归
            stack.pop()  # 撤销选择，目的下一个for循环元素的选择


if __name__ == '__main__':
    s = Solution()
    print(s.permute([1, 2, 3]))
