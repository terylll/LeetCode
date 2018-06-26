class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        """
        Greedy
        """
        
        maxLen = 1
        curLen = 1
        for i in range(1, len(nums)):
            if (nums[i] > nums[i - 1]):
                curLen += 1
                if (curLen > maxLen):
                    maxLen = curLen
            else:
                curLen = 1
        return maxLen if len(nums) > 0 else 0
        