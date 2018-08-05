import sys
import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        """
        d[i]: least number of perfect squares that sum to n

        d[i] = min(d[i - j*j] + 1) for j in (1 .. sqrt(i))
        """

        d = [sys.maxint for i in range(n+1)]

        d[0] = 0

        for i in range(1, n + 1):
            for j in range(1, int(math.sqrt(n))):
                d[i] = min(d[i], d[i - j*j] + 1)
        
        return d[n]

sol = Solution()
print(sol.numSquares(12))
