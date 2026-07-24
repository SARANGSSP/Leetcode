class MinStack:

    def __init__(self):
        self.stack = []
        self.head = -1
        self.mini = float("inf")


    def push(self, value: int) -> None:
        self.stack.append(value)
        self.head += 1
        self.mini = min(self.mini,value)

    def pop(self) -> None:
        if self.head == -1:
            return None
        else:
            self.head -= 1
            a = self.stack.pop()
            if a == self.mini:
                if len(self.stack) == 0:
                    self.mini = float("inf")
                    return None
                else:
                    self.mini = min(self.stack)
            return a      

    def top(self) -> int:
        return self.stack[self.head]

    def getMin(self) -> int:
        return self.mini


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()