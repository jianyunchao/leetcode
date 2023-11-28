from typing import List


class Solution(object):
    def nextGreaterElement2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # map_list = []
        # for num in nums1:
        #     map_list.append(nums2.index(num))
        # print(map_list)
        #
        # stack = []
        # res = [-1] * len(nums2)
        # stack.append(nums2[0])
        # for i in range(1, len(nums2)):
        #     while stack and nums2[i] > nums2[stack[-1]]:
        #         pop = stack.pop()
        #         res[pop] = i
        #     stack.append(i)
        #     # 1 3 4 2

        stack = []
        res_map = {}
        res = [0] * len(nums2)
        # for num in reversed(nums2):
        for i in range(len(nums2) - 1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            res_map[nums2[i]] = stack[-1] if stack else -1
            res[i] = stack[-1] if stack else -1
            stack.append(nums2[i])
        return [res_map[n] for n in nums1]


class Solution:
    def nextGreaterElement3(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [0] * len(nums2)
        stack = []
        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                res[stack.pop()] = i
            stack.append(i)
        return [res[nums2.index(num)] for num in nums1]


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = {}
        stack = []
        for num in reversed(nums2):
            while stack and num >= stack[-1]:
                stack.pop()
            res[num] = stack[-1] if stack else -1
            stack.append(num)
        return [res[num] for num in nums1]


if __name__ == '__main__':
    # 输入：nums1 = [4,1,2], nums2 = [1,3,4,2].  [1,2,0,0]
    # 输出：[-1,3,-1]
    s = Solution()
    print(s.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
    # 2 s=0 r=-1 s=2
    # 2 4  s=2 r=-1 s=4
    # 2 4 3 s=4 r=4 s=4,3
    # 2 4 3 1 s=4,3 r=3 s=4,3
