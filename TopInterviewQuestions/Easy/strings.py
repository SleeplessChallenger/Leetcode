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




