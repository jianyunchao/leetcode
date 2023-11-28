class MinStack:

    def __init__(self):
        self.main = []
        self.back = []
        self.min = 2 ** 31

    def push(self, val: int) -> None:
        self.main.append(val)
        if val <= self.min:
            self.back.append(val)
            self.min = val

    def pop(self) -> None:
        p = self.main.pop()
        if self.back and p == self.back[-1]:
            self.back.pop()
            if self.back:
                self.min = self.back[-1]  # 可能为空
        return p

    def top(self) -> int:
        return self.main[-1]

    def getMin(self) -> int:
        if len(self.main) == 1:  # 只有一个元素，自身最小
            return self.main[-1]
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())
    minStack.pop()
    print(minStack.top())
    print(minStack.getMin())
