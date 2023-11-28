from typing import List


class Solution:
    def dailyTemperatures_r(self, temperatures: List[int]) -> List[int]:
        s = []
        r = [None] * len(temperatures)
        for i in range(len(temperatures) - 1, -1, -1):
            # while s and temperatures[i] >= s[-1]:  # 存放索引，拿值出来比较
            while s and temperatures[i] >= temperatures[s[-1]]:  # 等于也要出栈清空，不是大于
                s.pop()
            r[i] = s[-1] - i if s else 0  # 逆序，以i为准
            s.append(i)
        return r

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        r = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while s and temperatures[i] > temperatures[s[-1]]:
                j = s.pop()
                r[j] = i - j  # 正序，以s里面为准
            s.append(i)
        return r


if __name__ == '__main__':
    s = Solution()
    print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 73, 73]))
    print(s.dailyTemperatures_r([73, 74, 75, 71, 69, 72, 73, 73]))
