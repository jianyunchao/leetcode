class NumArray(object):

    # def __init__(self, nums):
    #     """
    #     :type nums: List[int]
    #     """
    #     self.nums = nums
    #     self.pre_sum = self.get_prefix_sum(nums)
    #
    # def sumRange(self, left, right):
    #     """
    #     :type left: int
    #     :type right: int
    #     :rtype: int
    #     """
    #     return self.pre_sum[right + 1] - self.pre_sum[left]

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self._pre_sum = [0]
        for num in nums:
            self._pre_sum.append(self._pre_sum[-1] + num)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        # return self.pre_sum[right + 1] - self.pre_sum[left]
        return self._pre_sum[right + 1] - self._pre_sum[left]

    def get_prefix_sum(self, nums):
        pre_sum = [0] * (len(nums) + 1)
        pre_sum[1] = nums[0]
        for x in range(1, len(nums) + 1):
            pre_sum[x] = pre_sum[x - 1] + nums[x - 1]
        return pre_sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

if __name__ == '__main__':
    n = NumArray([-2, 0, 3, -5, 2, -1])
    print(n.sumRange(0, 2))
    print(n.sumRange(2, 5))
    print(n.sumRange(0, 5))
