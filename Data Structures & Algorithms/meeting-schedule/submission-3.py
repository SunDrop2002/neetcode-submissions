"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals,
                           key= lambda x: x.start)
        for i in range(len(intervals)-1):
            end_1 = intervals[i].end
            start_2 = intervals[i+1].start

            if end_1 > start_2:
                return False
        
        return True  
