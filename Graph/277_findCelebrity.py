# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        candidate = 0
        for i in range(n):
            if (knows(candidate, i) is True):
                candidate = i
        
        # If all people know candidate
        for i in range(n):
            if (knows(i, candidate) is False):
                return -1
        # If candidate don't know all people
        for i in range(candidate):
            if (knows(candidate, i) is True):
                return -1
                
        return candidate