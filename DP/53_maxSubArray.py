"""
Link: https://leetcode.com/problems/maximum-subarray/description/
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """
        dp[i]: the max sum of sub array in A[0 ... i] such that the sub array ends at [i]

        dp[i] = max( dp[i - 1] + val[i], val[i])

        Note:
        The maximum sub array that ends at A[i] either includes A[0 ... i - 1] or doesn't.
        """

        if (len(nums) == 0):
            return 0

        global_max = nums[0]
        cur_max = nums[0]

        for i in range(len(nums)):
            cur_max = max(cur_max + nums[i], nums[i])
            global_max = max(global_max, cur_max)
        
        return global_max
