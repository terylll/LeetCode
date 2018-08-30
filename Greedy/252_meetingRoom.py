# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        # Sort by start time
        intervals.sort(key = lambda x: x.start)
        
        for i in range(1, len(intervals)):
            if (intervals[i - 1].end > intervals[i].start):
                return False
        
        return True

sol = Solution()
sol.canAttendMeetings([[0,30],[5,10],[15,20]])