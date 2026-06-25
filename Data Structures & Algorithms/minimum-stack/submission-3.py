class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack =[]
        self.min = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min > val:
            self.min = val
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        if(len(self.min_stack) > 0):
            self.min = self.min_stack[-1]
        else:
            self.min = float('inf')

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        
