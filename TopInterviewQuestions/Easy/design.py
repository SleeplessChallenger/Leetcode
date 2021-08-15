# 1. Min Stack
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.MinStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.MinStack) == 0:
            self.MinStack.append({'min': val})
        else:
            minNum = self.MinStack[-1]['min'] if self.MinStack[-1]['min'] < val else val
            self.MinStack.append({'min': minNum})
        

    def pop(self) -> None:
        self.MinStack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.MinStack[-1]['min']
