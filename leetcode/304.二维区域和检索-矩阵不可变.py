class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.pre_sum = [[] * len(matrix)]
        m, n = len(matrix), len(matrix[0])
        if m == 0 or n == 0: return
        self.pre_sum = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.pre_sum[i][j] = self.pre_sum[i - 1][j] + self.pre_sum[i][j - 1] + matrix[i - 1][j - 1] - \
                                     self.pre_sum[i - 1][j - 1]
        print(self.pre_sum)

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.pre_sum[row2 + 1][col2 + 1] - self.pre_sum[row1][col2 + 1] - self.pre_sum[row2 + 1][col1] + \
            self.pre_sum[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
matrix = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
obj = NumMatrix(matrix)
print(obj.sumRegion(1, 1, 2, 2))
# print(obj.sumRegion(1, 1, 2, 2))
# print(obj.sumRegion(1, 2, 2, 4))
