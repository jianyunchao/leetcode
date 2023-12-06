from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float("inf")
        left = 0
        sum = 0
        for right, x in enumerate(nums):
            sum += x
            while sum - nums[left] >= target:  # 先判断是否可以减
                sum -= nums[left]  # 先操作，再移动指针
                left += 1
            if sum >= target:
                ans = min(ans, right - left + 1)
        return ans


if __name__ == '__main__':
    s = Solution()
    s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
