# 1. Reverse String
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1
        while i <= j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

# 2. Reverse Integer
class Solution:
    def reverse(self, x: int) -> int:
        # as we have 32-bit constraint => check it
        if 2 ** 31 - 1 <= x or -2 ** 31 >= x:
            return 0
        else:
            strNum = str(x)
            if x >= 0:
                reversedStr = strNum[::-1]
            else:
                without_minus = strNum[1:]
                reversedStr = without_minus[::-1]
                reversedStr = '-' + reversedStr
        
        if int(reversedStr) >= 2**31 - 1 or int(reversedStr) <= -2**31:
            return 0
        else:
            return int(reversedStr)

# 3. First Unique Character in a String
class Solution:
    def firstUniqChar(self, s: str) -> int:
        ht = {}
        for char in s:
            if char not in ht:
                ht[char] = 0
            ht[char] += 1
        
        for idx in range(len(s)):
            letter = s[idx]
            if ht[letter] == 1:
                return idx
        
        return -1

# 4. String to Integer (atoi)
class Solution:
    def myAtoi(self, s: str) -> int:
        # remove leading whitespaces
        # but we don't need counter
        # as we'll remove each whitespace
        if len(s) < 1:
            return 0
        
        # `while s` is when input is: " "
        while s and s[0] == ' ':
            s = s[1:]
        
        if len(s) < 1:
            return 0
        
        isChar = s[0] == '-' or s[0] == '+'
        isMinus = s[0] == '-'
        # we need to remove leading minus/plus if such is
        s = s[1:] if isChar else s
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        result = []
        i = 0
        while i < len(s):
            token = s[i]
            if token not in digits:
                break
            result.append(token)
            i += 1
        
        if len(result) < 1:
            return 0
        
        fullInteger = int(''.join(result))
        withMinus = -fullInteger if isMinus else fullInteger
        
        return self.clamp(withMinus, -2**31, 2**31 - 1)
    
    def clamp(self, num, smallest, largest):
        return max(smallest, min(num, largest))

# 1. Read in and ignore any leading whitespace.

# 2. Check if the next character (if not already at the end of the string) is '-' or '+'.
#	Read this character in if it is either. This determines if the final result is negative or positive respectively.
#	Assume the result is positive if neither is present.

# 3. Read in next the characters until the next non-digit charcter or the end of the input is reached.
#	The rest of the string is ignored.

# 4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32).
#	If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).

# 5. If the integer is out of the 32-bit signed integer range [-231, 231 - 1],
#	then clamp the integer so that it remains in the range.
#	Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.

# 6. Return the integer as the final result.

# 5. Implement strStr()

class Solution:
    
    # One-liner
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
    
    
    # KMP
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) ==  0 and len(needle) ==  0:
            return 0
        if len(needle) == 0:
            return 0
        
        pattern = self.buildPattern(needle)
        return self.isValid(pattern, haystack, needle)
        
    def buildPattern(self, needle):
        pattern = [-1 for _ in needle]
        i = 1
        j = 0
        while i < len(needle):
            if needle[i] == needle[j]:
                pattern[i] = j
                i += 1
                j += 1
            elif j > 0:
                j = pattern[j - 1] + 1
            else:
                i += 1
                
        return pattern
    
    def isValid(self, pattern, big, small):
        i = j = 0
        while i + len(small) - j <= len(big):
            if big[i] == small[j]:
                if j == len(small) - 1:
                    return i - j
                i += 1
                j += 1
            elif j > 0:
                j = pattern[j - 1] + 1
            else:
                i += 1
        return -1

# 6. Longest Common Prefix
class Solution:
    # Horizontal scanning
    # 1. take first word from the list
    # 2. first iteration will skip, but in the second
    # we'll cut by one from the end if new word doesn't
    # start with all the substring of the old word.
    # 3. old word will persist through all words in the list
    # hence in result we'll get desired output (prefix )
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        prefix = strs[0]
        for idx in range(1, len(strs)):
            string = strs[idx]
            while string.startswith(prefix) == False:
                prefix = prefix[:-1]
        
        return prefix
    
    # Divide & Coqnuer
    # Time: O(m * logN) where m is the largest string
    # and logN is a recursive call stack
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0 or len(strs) == 1:
            return strs[0]
        
        return self.divide_conquer(strs)
        
    def divide_conquer(self, strings):
        if len(strings) == 1:
            return strings[0]
        
        leftPart = self.divide_conquer(strings[:len(strings) - 1])
        rightPart = self.divide_conquer(strings[len(strings) - 1:])
        return self.gist_function(leftPart, rightPart)
        # `return` from here will give common prefix
        # to leftPart
    
    def gist_function(self, left, right):
        min_length = min(len(left), len(right))
        # min_length == len(smallest) - 1
        # => we can return :idx as this idx
        # we'll be out of range already
        # and python is exclusive
        for i in range(min_length): # O(m)
            if left[i] != right[i]:
                return left[:i]
     
        return left[:min_length]

# 7. Count and Say
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == '0':
            return ""
        if n == '1':
            return "1"
        
        result = '1'
        for i in range(n - 1):
            prev, count = result[0], 0
            temp = ""
            
            for j in result:
                if j == prev:
                    count += 1
                else:
                    temp += str(count) + prev
                    prev = j
                    count = 1
            
            temp += str(count) + prev
            result = temp
        
        return result
