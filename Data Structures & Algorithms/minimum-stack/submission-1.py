class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0 and len(self.minStack) == 0:
            self.stack.append(val)
            self.minStack.append(val)

        else:
            if self.minStack[-1] > val:
                self.minStack.append(val)
            else:
                minV = self.minStack[-1]
                # Value here is reapted push again as new min at that level
                self.minStack.append(minV)
            self.stack.append(val)
        
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

        

    def getMin(self) -> int:
        return self.minStack[-1]
        
