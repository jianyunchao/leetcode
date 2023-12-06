from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans = len(nums)
        left = 0
        if ans <= 1:
            return 0
        product = 1
        for right, x in enumerate(nums):
            product *= x
            while product >= k:
                product /= nums[left]
                left += 1
            ans += right - left + 1
        return ans