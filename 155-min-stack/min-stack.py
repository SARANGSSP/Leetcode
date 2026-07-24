class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []


    def push(self, value: int) -> None:
        if len(self.stack) == 0 and len(self.minstack) == 0:
            self.minstack.append(value)
        elif value <= self.minstack[-1]:
            self.minstack.append(value)
        self.stack.append(value)

    def pop(self) -> None:
        if len(self.stack) != 0: 
            a = self.stack.pop()
            if len(self.minstack) != 0 and a == self.minstack[-1]:
                self.minstack.pop()    

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.minstack) != 0:
            return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()