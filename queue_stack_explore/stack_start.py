# 1. Daily Temperatures
class Solution:
    '''
    1. create `ans` array prepopulated with 0
    2. traverse input array
    3. if len(stack) != 0 and current temp
        bigger that last on stack =>
    
    4. take difference in indicies and put it
        in place of idx from the stack (that
        we popped)
    
    5. at the bottom add curr idx
    '''
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0 for _ in temperatures]
        stack = []
        
        for i in range(len(temperatures)):
            val = temperatures[i]
            
            while len(stack) != 0 and val > temperatures[stack[-1]]:
                nodeIdx = stack.pop()
                diff = i - nodeIdx
                ans[nodeIdx] = diff
            
            stack.append(i)
        
        return ans

# 2. Evaluate Reverse Polish Notation
# Time: O(n) Space: O(d)
class Solution:
    # mine
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0
        operators = ['+', '-', '*', '/']
        
        for t in tokens:
            if t in operators:
                self.make_computations(t, stack)
            else:
                stack.append(int(t))

        return stack[0]
    
    def make_computations(self, t, stack):
        num1 = stack.pop()
        num2 = stack.pop()
        
        if t == '+':
            result = num1 + num2
        elif t == '-':
            result = num2 - num1
        elif t == '*':
            result = num1 * num2
        elif t == '/':
            # int() + / 
            result = int(num2 / num1)
            
        stack.append(result)
    
    # not mine
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            '+': lambda x,y: x + y,
            '-': lambda x,y: x - y,
            '*': lambda x,y: x * y,
            '/': lambda x,y: int(x / y)
        }
        
        for t in tokens:
            if t in operators:
                num2 = stack.pop()
                num1 = stack.pop()
                op = operators[t]
                stack.append(op(num1, num2))
            else:
                stack.append(int(t))
    
        return stack.pop()
