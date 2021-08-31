# medium chunk
# 1. Merge Intervals
class Solution:
	'''
    in first `if` we modify interval already
    in the list, whilst in the second we `.append()`
    it and now prev becomes curr => for the next iteration
    if first `if` works => it'll be modified in-place
    '''
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        
        intervals.sort(key=lambda x: x[0])
        prev = intervals[0]
        result = [ prev]
        
        for curr in intervals:
            if curr[0] <= prev[1]:
                prev[1] = max(prev[1], curr[1])
            else:
                prev = curr
                result.append(prev)

        return result

# 2. Insert Interval
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        
        # as `intervals` already sorted, we can
        # make a couple of edge checks
        for idx in range(len(intervals)):
            if intervals[idx][0] > newInterval[1]:
                result.append(newInterval)
                return result + intervals[idx:]
            
            elif intervals[idx][1] < newInterval[0]:
                result.append(intervals[idx])
            
            else:
            # elif intervals[idx][1] >= newInterval[0] and\
            #   intervals[idx][0] <= newInterval[1]:
                
                newInterval = [min(newInterval[0], intervals[idx][0]),
                              max(newInterval[1], intervals[idx][1])]
        
        # as we break out of `for` only in case
        # we didn't enter first check => append
        # newInterval
        result.append(newInterval)
        return result
