# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        
        if (len(intervals) == 0):
            return 0
        
        intervals.sort(key = lambda x: x.end)
        rooms = []
        rooms.append([])
        for i in range(len(intervals)):
            opt = None
            for j in range(len(rooms)):
                if (len(rooms[j]) == 0 or rooms[j][-1].end <= intervals[i].start):
                    if (opt is None or rooms[opt][-1].end < rooms[j][-1].end):
                        opt = j
            
            if (opt is None):
                rooms.append([intervals[i]])
            else:
                rooms[opt].append(intervals[i])
        
        return len(rooms)

sol = Solution()
print(sol.minMeetingRooms)
            