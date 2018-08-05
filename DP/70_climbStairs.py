class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        """
        Base Case:

        p[0] = 0
        p[1] = 1
        p[2] = 2

        DP:
        p[i] = p[i - 1] + p[i - 2]
        """

        p = [0 for i in range(n + 1)]

        p[0] = 0
        p[1] = 1
        p[2] = 2

        for i in range(3, n + 1):
            p[i] = p[i - 1] + p[i - 2]
        
        return p[i]