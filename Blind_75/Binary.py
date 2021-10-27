# 1. easy - Number of 1 bits
class Solution:
	# first
    def hammingWeight(self, n: int) -> int:
        count =  0
        while n:
            n = n & (n - 1)
            count += 1
            
        return count

    # second
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')

    # third
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n & 1
            # 1 & 1 = 1; 1 & 0 = 0
            n >>= 1
        return res

# 2. easy - missing number
class Solution:
    
    # Time: O(n) Space: O(n) using hashing
    def missingNumber(self, nums: List[int]) -> int:
        ht = {}
        i = 0
        while i <= len(nums):
            ht[i] = True
            i += 1
        
        for num in nums:
            del ht[num]
        
        return list(ht.keys())[0]
    
    # Time: O(n) Space: O(1) using XOR
    # 2 in binary is 10, 3 in binary is 11
    # 1 ^ 1 => 0; 0 ^ 0 => 0. So,if similar -> 0
    # 1 ^ 0 => 1;  0 ^ 1 => 1. So, if different -> 1
    # PS: ^ means XOR
    # Hence, 5 ^ 5 ^ 3. 5 ^ 5 -> 0, 5 ^ 3 -> 3 
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        for i, num in enumerate(nums):
            length ^= i ^ num
        
        return  length

    
    # Time: O(n) Space: O(1)  using sum
    # 1. place length of array
    # 2. traverse 
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        for i in range(len(nums)):
            # i is our number
            length += i - nums[i]
        
        return length

    # using set
    # Time: O(n) Space: O(n) using hashing
    def missingNumber(self, nums: List[int]) -> int:
        allNums = set(nums)
        length = len(nums) + 1
        # as one is missing -> add one
        for i in range(length):
            if i not in allNums:
                return i

# 3. easy - reverse bits
class Solution:
    def reverseBits(self, n: int) -> int:
        '''
        1. to figure out the last number we use
            `&`: number & 1.
            Ex: 0 & 1 = 0; 1 & 1 = 1
        
        2. But we also need to shift bits in n. How can
            we do so> => `>>`.
            As we apply & with >> to get the curr bit
        
        3. In our `result` we'll check with logic or: |;
            as we want 0 if curr is 0 else 1.
            But simple | isn't enough as we want to shift
            position as well.
            
            Look that at first we shift right and in result
            we shift left
            => get first bit of n and put it in 31 place
                of our result and so on
            
        '''
        result = 0
        # all 32 bits are o at first
        
        for i in range(32):
            temp = (n >> i) & 1
            result = result | (temp << (32 - (i + 1)))
        
        return result

# 4. easy - counting bits
class Solution:
    
    # with bin()
    # def countBits(self, n: int) -> List[int]:
    #     # number of 1 in a binary
    #     # representation of an integer
    #     return [bin(num).count('1') for num in range(n + 1)]
    
    # dynamic programming
    def countBits(self, n: int) -> List[int]:
    # For 0-3 & 4-7 range two last bits are the same
    # in pairs (0 & 4, 3 & 7 etc), but third from the end
    # is the `most significant one`that has 1:
    # 1 + dp[n - 4] -> how many `1` are in the last two
    # positions
    # 2: 0010
    # 3: 0011
    # as if we look at binary representation
    # of every figure, then they have pattern
    # for every range within 4. Ex: 1 & 5, 3 & 7 etc
    
    # this `-number` is an offset = most significant
    # bit we've reached so far. Most significant beats:
    # [1, 2, 4, 8, 16 ...]
    
        dp = [0 for _ in range(n + 1)]
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]

        return dp

# Medium chunk
# 1. Sum of 2 integers
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        
        while b & mask > 0:
            carry = (a & b)
            a = (a ^ b)
            b = carry << 1
        
        return (a & mask) if b > 0 else a
