"""
Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        """
        Two Pointer
        """
        """
        TODO: 
            if not assumed exactly one solution exist
            if can use same element more than once
        """
        low = 0
        high = len(numbers) - 1
        res = numbers[low] + numbers[high]
        while (res != target):
            if (res > target):
                high -= 1
            elif (res < target):
                low += 1
            
            res = numbers[low] + numbers[high]
        return [low + 1, high + 1]
        