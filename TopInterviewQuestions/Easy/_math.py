# 1. FizzBuzz
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        if n == 1:
            return ['1']
        
        result = []
        for idx in range(1, n + 1):
            if idx % 3 == 0 and idx % 5 == 0:
                result.append('FizzBuzz')
            elif idx % 3 == 0:
                result.append('Fizz')
            elif idx % 5 == 0:
                result.append('Buzz')
            else:
                result.append(str(idx))
        
        return result

# 2. Count Primes
class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [True for _ in range(n)]
        count = 0
        
        for i in range(2, n):
            if primes[i]:
                count += 1
                for j in range(i, n, i):
                    primes[j] = False
        
        return count

# 3. Power of Three
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        i = 1
        while i < n:
            i *= 3
        
        return True if i == n else False

# 4. Roman to Integer
class Solution:
    def romanToInt(self, s: str) -> int:
        ht = {          'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        
        total = 0
        prev = 0
        
        for token in s:
            num = ht[token]
            total += num
            if num > prev:
                subtract = prev * 2
                total -= subtract
            
            prev = num

        return total
