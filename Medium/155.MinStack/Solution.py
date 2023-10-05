class MinStack:
    #Time Complexity - O(1)
    #Space Complexity - O(N)
    def __init__(self):
        self.stack = []
        self.min_values = [] 

    def push(self, val: int) -> None:
        if not self.min_values:
            self.min_values.append(val)
        elif self.min_values[-1] >= val:
            self.min_values.append(val)
        self.stack.append(val)
        

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min_values[-1]:
            self.min_values.pop()
        return val
        

    def top(self) -> int:
        return self.stack[- 1]

    def getMin(self) -> int:
        return self.min_values[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()