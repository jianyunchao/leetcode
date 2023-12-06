class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        window = {}
        left, right = 0, 0
        res = -1
        while right < len(s):
            c = s[right]
            right += 1
            window[c] = window.get(c, 0) + 1

            # while left < right & window.count(s[right]) >= 1:
            #     left -= 1
            while window[c] > 1:
                d = s[left]
                left += 1
                window[d] -= 1

            res = max(res, right - left)

        return res


if __name__ == '__main__':
    s = Solution()
    string = "abcabcbb"
    print(s.lengthOfLongestSubstring(string))
