class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if not intervals:
            return []
        # sort the intervals
        sorted_intervals = sorted(intervals)

        # overlap by comparing each last interval appeneded 
        # with the current interval
        result = [sorted_intervals[0]]
        for i in range(1,len(sorted_intervals)):
            last_merged = result[-1]
            if sorted_intervals[i][0] <= last_merged[1]:
                start = last_merged[0]
                end = max(last_merged[1],sorted_intervals[i][1])
                result[-1] = [start,end]
            else:
                result.append(sorted_intervals[i])
        
        return result
