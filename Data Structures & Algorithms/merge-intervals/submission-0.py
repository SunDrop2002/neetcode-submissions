class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the intervals
        sorted_intervals = sorted(intervals)

        # overlap by comparing each last interval appeneded 
        # with the current interval
        result = [sorted_intervals[0]]
        for i in range(1,len(sorted_intervals)):
            current_interval = result[-1]
            if sorted_intervals[i][0] <= current_interval[1]:
                start = current_interval[0]
                end = max(current_interval[1],sorted_intervals[i][1])
                result[-1] = [start,end]
            else:
                result.append(sorted_intervals[i])
        
        return result
