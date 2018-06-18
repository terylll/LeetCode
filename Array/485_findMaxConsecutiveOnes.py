class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        counter = 0
        maxCounter = 0
        for i in range(len(nums)):
        	if nums[i] == 1:
        		counter += 1
        	else:
        		counter = 0

        	"""
        	Edge case:
        		nums = [1]
        		output = 1
        		check maxCounter in every iterations
        	"""
        	if counter > maxCounter:
        			maxCounter = counter
        return maxCounter