"""
Link: https://leetcode.com/problems/min-cost-climbing-stairs/description/
"""

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
        p = [0 for i in range(len(cost))]
        p[-1] = cost[-1]
        p[-2] = cost[-2]

        for i in range(len(cost) - 3, -1, -1):
            p[i] = cost[i] + min(p[i + 1], p[i + 2])
        return min(p[0], p[1])

sol = Solution()

print sol.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])