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
