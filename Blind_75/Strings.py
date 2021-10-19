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

# Medium chunk

# 1. medium - Longest Palindromic Substring
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = [0, 1]
        for idx in range(1, len(s)):
            first_case = self.check_substring(idx - 1, idx + 1, s)
            second_case = self.check_substring(idx - 1, idx, s)
            longest_case = max(first_case, second_case, key=lambda x: x[1] - x[0])
            longest = max(longest_case, longest, key=lambda x: x[1] - x[0])
        return s[longest[0]:longest[1]]

    def check_substring(self, idx1, idx2, string):
        while idx1 >= 0 and idx2 < len(string):
            if string[idx1] != string[idx2]:
                break
            idx1 -= 1
            idx2 += 1
            
        return [idx1 + 1, idx2]

# 2. Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        ht = {}
        longest = [0, 1]
        start = 0
        
        for idx in range(len(s)):
            letter = s[idx]
            if letter in ht:
                start = max(start, ht[letter] + 1)
            if longest[1] - longest[0] < idx - start + 1:
                longest = [start, idx + 1]
            ht[letter] = idx
        
        return longest[1] - longest[0]

# 3. Encode and Decode Strings
# brute-force
class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        if len(strs) == 0:
            return chr(258)
        
        result = chr(257).join(strs)
        return result
        
        

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        if s == chr(258):
            return []
        
        return s.split(chr(257))

# optimal
# all you need to do is encode the length of x into 4 bytes ( why 4 bytes - integer size - 4 bytes = [8bits, 8bits, 8bits, 8bits])

# ok so how do you get a X(length of str) total size into chunks of 8 bits ?
# 2.1 >> is right shift - which means if you have 101111 >> 2 - this right shift moves 101111, 2 times to the right - which
# becomes 1011
# 2.2 if you go to python terminal and type 0xff you get 8 1's which represents 11111111 = a BYTE
# 2.3 if you AND(&) any number with 0xff = it gives you the right most 8 bits of the number
# example: 1. bin(291) (binary of 291) is '0b100100011'
# 2. oxff binary is '0b11111111'
# 3. now if you 291 & 0xff = you get last 8 bits of 291 == 00100011
# If you understand this - you understood the solution.

# Now as explained in the 2 point. The python solution line 6 we take the whole length of the string (len(str)) - we have to
# encode that into [8bits, 8 bits, 8bits, 8bits]
# example: 1. lets say our total length is 291 ( in binary its bin(291) = '0b100100011')
# 2. what you have to do now ? we grab the right most 8 bits - how do you grab right most 8 bits ?
# 2.1 as mentioned above you do 291 & 0xff = you get last 8 bits

# Now you already have right most 8 bits - in next iteration you are interested in NEXT 8 bits - how do you get
# that ? we move 291 >> 8 ( which removes the last 8 bits we already computed) - which means if you do
# (291 >> 8 ) & 0xff = it gives you the next right most 8 bits

# as already mentioned we need 4 chunks of 8 bits [8bits, 8bits, 8bits, 8bits]
# 4.1 [ for i in range(4)] thats why the range is 4 ( 0, 1, 2, 3)

# Once you compute all the 8bits we need to convert to char hence its [chr((x >> (i * 8)) & 0xff) for i in range(4)]

# 4. Longest Repeating Character Replacement
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        1. most frequent character and check that: 
            window_size - this => under/equal `k`. Why? => 
            we're to find whether we can use existing
            number of `k` flips to make longest substring.
        
        2. "AABABBA". Take part: AABA. window_size = 4.
            ht = {'A': 3, 'B': 1}. temp = 4 - 3 => 1. 1 <= k(1)
            Hence we can use our 1 flip to change the letter and
            to create longest subsequence
            
        '''
        left = 0
        right = 0
        
        ht = {}
        longest = 0
        
        while right < len(s):
            letter = s[right]
            if letter not in ht:
                ht[letter] = 0
            
            ht[letter] += 1
            
            max_count = self.get_max(ht)

            cells_count = right - left + 1
            # +1 as we're to have full substring
            temp = cells_count - max_count
            
            if temp <= k:
                longest = max(longest, cells_count)
                
            else:
                letter = s[left]
                
                ht[letter] -= 1
                if not ht[letter]:
                    # del ht[letter]
                    ht.pop(letter)
                
                left += 1
            
            right += 1
            
        return longest
    
    def get_max(self, ht):
        return max(ht.values())

# 5. Palindromic Substrings
class Solution:
    def countSubstrings(self, string: str) -> int:
        result = 0
        
        for x in range(len(string)):
            odd = self.func(string, x, x)
            even = self.func(string, x-1, x)
            # self.func(string, x, x+1)
            
            result += odd
            result += even
            
        return result
        
    def func(self, string, i, j):
        # we start from 0 as we are okay
        # when counting `odd` to have 1,
        # but when counting `even`: we
        # may not have a palindrome
        curr = 0
        while i >= 0 and j < len(string):
            if string[i] != string[j]:
                break
            
            curr += 1
            i -= 1
            j += 1
            
            
        return curr

        l = 0
        c_frequency = {}
        longest_str_len = 0
        for r in range(len(s)):
            
            if not s[r] in c_frequency:
                c_frequency[s[r]] = 0
            c_frequency[s[r]] += 1
            
            # Replacements cost = cells count between left and right - highest frequency
            cells_count = r - l + 1
            if cells_count - max(c_frequency.values()) <= k:
                longest_str_len = max(longest_str_len, cells_count)
                
            else:
                c_frequency[s[l]] -= 1
                if not c_frequency[s[l]]:
                    c_frequency.pop(s[l])
                l += 1
        
        return longest_str_len


# Hard
# 6. Minimum Window Substring
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ht = self.get_ht(t)
        s_e = self.get_pointers(ht, s, t)
        return self.get_result(s_e, s)
        
        
    def get_ht(self, string):
        ht = {}
        for s in string:
            if s not in ht:
                ht[s] = 0
            ht[s] += 1
        
        return ht
    
    def get_result(self, limit, string):
        if limit[1] == float('inf'):
            return ""
        return string[limit[0]:limit[1] + 1]
    
    def get_pointers(self, ht, bigString, smallString):
        bounds = [0, float('inf')]
        
        leftP = 0
        rightP = 0
        
        big_ht = {}
        marked = 0
        unique_letters = len(ht.keys())
        
        # move right pointer
        while rightP < len(bigString):
            letter = bigString[rightP]
            
            if letter not in ht:
                rightP += 1
                continue
            
            if letter not in big_ht:
                big_ht[letter] = 0
            big_ht[letter] += 1
            
            if big_ht[letter] == ht[letter]:
                marked += 1
            
            # move left pointer
            while unique_letters == marked and leftP <= rightP:

                letter = bigString[leftP]

                bounds = self.check_bounds(leftP, rightP,
                        bounds[0], bounds[1])

                # this can be letter that isn't
                # in our small ht => go further
                if letter not in ht:
                    leftP += 1
                    continue


                if big_ht[letter] == ht[letter]:
                    marked -= 1

                big_ht[letter] -= 1
                leftP += 1

            rightP += 1
 
        return bounds
                
    def check_bounds(self, idx1, idx2, idx3, idx4):
        return [idx1, idx2] if (idx2 - idx1) < (idx4 - idx3)\
            else [idx3, idx4]
