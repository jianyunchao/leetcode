from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        q = deque()
        for i, x in enumerate(nums):
            # 1 入
            while q and nums[q[-1]] <= x:  # 单调递减，队首最大
                q.pop()
            q.append(i)
            # 2 出
            if i - q[0] >= k:
                q.popleft()
            # 3 记
            if i >= k - 1:
                ans.append(nums[q[0]])
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
