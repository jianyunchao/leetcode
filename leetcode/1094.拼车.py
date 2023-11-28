class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        self.diff = []
        self.capacity = capacity
        for trip in trips:
            if trip[2] > len(self.diff):

                self.diff += [0] * (trip[2] - len(self.diff) + 1)
                print(self.diff)
            # self.increment(trip[1] - 1, trip[2] - 1, trip[0])
            self.increment(trip[1], trip[2] - 1, trip[0])
        return self.result()

    def diff(self):
        pass

    def increment(self, i, j, val):
        self.diff[i] += val
        # fixme
        # if j + 1 <= len(self.diff):
            # self.diff[j] -= val
        self.diff[j + 1] -= val

    def result(self):
        print(self.diff)
        res = [0] * len(self.diff)
        res[0] = self.diff[0]
        if res[0] > self.capacity: return False
        for i in range(1, len(self.diff)):
            res[i] = res[i - 1] + self.diff[i]
            if res[i] > self.capacity: return False
        print(res)
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.carPooling([[2, 1, 5], [3, 3, 7]], 5))
    # print(s.carPooling([[2, 1, 5], [3, 3, 7]], 4))
    # print(s.carPooling([[9, 0, 1], [3, 3, 7]], 4))
