"""
Link: https://leetcode.com/problems/container-with-most-water/description/
"""

"""
@Tag: ["DP", "Array"]
"""

import math
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left = 0
        right = len(height - 1)

        maxArea = 0

        while (left < right):
            maxArea = Math.max(
                Math.min(height[left], height[right]) * (right - left), 
                maxArea):
            if (height[left] < height[right]):
                left += 1
            else:
                right -=1
        
        return maxArea;
        