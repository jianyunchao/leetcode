class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        diff = [0] * n
        for booking in bookings:
            i = booking[0] - 1
            j = booking[1] - 1
            seat = booking[2]
            diff[i] += seat
            if j + 1 < len(diff):
                diff[j + 1] -= seat

        res = [0] * n
        res[0] = diff[0]
        for x in range(1, len(diff)):
            res[x] = res[x - 1] + diff[x]
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.corpFlightBookings([[1, 2, 10], [2, 3, 20], [2, 5, 25]], 5))
