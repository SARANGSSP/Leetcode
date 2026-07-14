class MinStack:

    def __init__(self):
        self.stack = []
        self.head = -1
        self.mini = float("inf")


    def push(self, value: int) -> None:
         self.head += 1
         self.stack.append(value)
         self.mini = min(self.mini,value)

    def pop(self) -> None:
        if self.head != -1:
            self.head -= 1
            a = self.stack.pop()
            if a == self.mini:
                if self.head > -1:
                    self.mini = min(self.stack)
                else:
                    self.mini = float("inf")

        else:
            self.mini = None
            return None

    def top(self) -> int:
        return self.stack[self.head]

    def getMin(self) -> int:
        if self.head > -1:
            return self.mini
        else:
            return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()