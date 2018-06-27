"""
Link: https://leetcode.com/problems/jump-game/description/
"""

"""
Tag: @Array @Greedy
"""

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        """
        Optimize:

        Max Distance Travel

        """

        i = 0

        while (i < len(nums) - 1):
            end = i + nums[i] + 1 if i + nums[i] + 1 < len(nums) else len(nums)

            curMax = i
            next_idx = i
            for j in range(i + 1, end):
                if j + nums[j] > curMax:
                    curMax = j + nums[j]
                    next_idx = j
            if next_idx == i:
                return False
            
            i = next_idx

        return True 

sol = Solution()
print(sol.canJump([2, 0]))