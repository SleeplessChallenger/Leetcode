# 1. Check If N and Its Double Exist
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if len(arr) < 2:
            return False
        ht = {}
        for i in range(len(arr)):
            ht[arr[i]] = i
        
        for i in range(len(arr)):
            num = arr[i]
            if num * 2 in ht and ht[num*2] != i:
                return True
        
        return False

# 2. Valid Mountain Array
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3: # no purpose if length < 3
            return False
        
        length = len(arr)
        idx = 0
        
        while idx + 1 < length and arr[idx] < arr[idx + 1]:
            idx += 1
        
        if idx == 0 or idx == length - 1: # it can't be peak or tail
            return False
        
        while idx + 1 < length and arr[idx] > arr[idx + 1]:
            idx += 1
        
        return idx == length - 1 # as there can be bigger value at the end
