from typing import List


class Solution:
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(enumerate(nums), key=lambda x: x[1])
        left, right = 0, len(nums) - 1
        while right > left:
            sum = sorted_nums[left][1] + sorted_nums[right][1]
            if sum == target:
                return [sorted_nums[left][0], sorted_nums[right][0]]
            elif sum > target:
                right -= 1
            elif sum < target:
                left += 1

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()

        for index, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], index]
            hashtable.setdefault(num, index)

        return [0]


if __name__ == '__main__':
    s = Solution()
    # print(s.twoSum([2, 7, 11, 15], 9))
    # print(s.twoSum([3, 2, 4], 6))
    print(s.twoSum([3, 3], 6))
