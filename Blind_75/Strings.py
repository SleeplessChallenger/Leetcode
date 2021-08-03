# 1. easy - Valid Palindrome
# slower
class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = self.convertString(s)
        return self.checkPalindrome(string)
    
    def checkPalindrome(self, string):
        if len(string) == 0 or len(string) == 1:
            return True
        elif string[0] == string[-1]:
            return self.checkPalindrome(string[1:-1])
        
        return False
        
    def convertString(self, string):
        return ''.join([x.lower() for x in string if x.isalnum()])
# faster
class Solution:   
    def convertString(self, string):
        return ''.join([x.lower() for x in string if x.isalnum()])
    
    def isPalindrome(self, s: str) -> bool:
        string = self.convertString(s)
        i = 0
        j = len(string) - 1
        while i <= j:
            if string[i] != string[j]:
                return False
            
            i += 1
            j -= 1
        
        return True

# 2. easy - Valid Anagram
# O(n*log n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        first = ''.join(sorted(s))
        second = ''.join(sorted(t))
        
        return first == second

# 3. easy - Valid Parentheses
# Time: O(n)  Space: O(n)
class Solution:
    def isValid(self, string: str) -> bool:
        stack = []
        match = {')': '(', ']': '[', '}': '{'}
        openBrackets = '([{'
        
        for token in string:
            if token in openBrackets:
                stack.append(token)
            else:
                if len(stack) == 0:
                    return False
                elif match[token] == stack[-1]:
                    stack.pop()
                else:
                    return False
                    
        return len(stack) == 0

# 4. easy - group anagrams
# Time: O(w * n * log n)
# w - number of words; n - longest word
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ht = {}
        
        for s in strs:
            string = ''.join(sorted(s))
            if string not in ht:
                ht[string] = []
                
            ht[string].append(s)
    
        return list(ht.values())
