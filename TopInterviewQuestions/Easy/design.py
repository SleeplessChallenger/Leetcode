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

# another ver.
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append({'min': val})
        else:
            curr_min = self.min_stack[-1]['min']
            result = min(curr_min, val)
            self.min_stack.append({'min': result})

    def pop(self) -> None:
        '''
        take list: [-2,0,-3]
        
        1. When -2 is pushed: it is in boths stacks in __inti__
        2. When 0 is pushed, 0 is in self.stack, but -2 again
            pushed to self.min_stack. Hence when we .pop() =>
            not only 0 is removed from stack, but that additional
            -2 in self.min_stack (as we have one more -2 before)
            is also removed
        '''
        self.min_stack.pop()
        self.stack.pop()
        
    '''
    if we don't have cases when
    two func below are called 
    and stack being empty
    '''
    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        return self.min_stack[-1]['min']
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# 2. Shuffle an Array
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prev = list(nums)
        # `list()` allows to create new list
        # whilst simple `=` will make those
        # lists interlinked
        
    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.nums = self.prev
        self.prev = list(self.prev)
        # here the same case as in `__ini__`
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """    
        for i in range(len(self.nums)):
            idx = random.randrange(i, len(self.nums))
            self.nums[i], self.nums[idx] = self.nums[idx], self.nums[i]
        
        return self.nums

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
