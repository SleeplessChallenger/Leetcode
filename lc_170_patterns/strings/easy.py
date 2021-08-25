# 1. Find Smallest Letter Greater Than Target
class Solution:
    # smallest that is larger. Array is sorted in increasing order.
    # Hence every next iteration will give bigger letter
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for letter in letters:
            if letter > target:
                return letter
        return letters[0]
       
    # if the target is bigger than every element => return first
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:  
        result = None
        for letter in letters:
            if self.isGreater(letter, target):
                if not result:
                    result = letter
                else:
                    result = min(letter, result, key=lambda x: ord(x))
                
        return result if result else letters[0]      
        
    def isGreater(self, letter, target):
        return ord(letter) > ord(target)


# 2. Backspace String Compare
class Solution:
    # Time: O(m + n) Space: O(m + n)
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        for i in s:
            if i != '#':
                stack1.append(i)
            elif len(stack1) != 0:
                stack1.pop()
        
        stack2 = []
        for j in t:
            if j != '#':
                stack2.append(j)
            elif len(stack2) != 0:
                stack2.pop()
        
        return ''.join(stack1) == ''.join(stack2)
    
    # Time: O(m + n) Space: O(1)
    def backspaceCompare(self, s: str, t: str) -> bool:
        countS = 0
        countT = 0
        
        i = len(s) - 1
        j = len(t) - 1
        
        while i >= 0 or j >= 0:
            while i >= 0:
                if s[i] == '#':
                    countS += 1
                    i -= 1
                elif countS > 0:
                    countS -= 1
                    i -= 1
                else:
                    break
            
            while j >= 0:
                if t[j] == '#':
                    countT += 1
                    j -= 1
                elif countT > 0:
                    countT -= 1
                    j -= 1
                else:
                    break
            
            # at first valid indicies check
            # as we can get error otherwise
            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False
            
            if (i >= 0) != (j >= 0):
                return False
            
            i = i - 1
            j = j - 1
        
        return True
