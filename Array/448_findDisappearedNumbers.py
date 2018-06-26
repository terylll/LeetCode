"""
Link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
"""

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if (nums[index] > 0):
                nums[index] = -nums[index]
        
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]
        
sol = Solution()

print sol.findDisappearedNumbers([4,3,2,7,8,2,3,1])

