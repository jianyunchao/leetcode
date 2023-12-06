class Solution:
    def isValid(self, s: str) -> bool:
        valid_map = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []

        for c in s:
            if c in valid_map:
                if stack and stack.pop() != valid_map[c]:
                    return False
            else:
                stack.append(c)
        if stack:
            return False
        else:
            return True


if __name__ == '__main__':
    s = Solution()
    print(s.isValid("()[]{}"))
    print(s.isValid("(]"))
