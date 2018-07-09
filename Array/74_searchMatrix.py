"""
Link: https://leetcode.com/problems/search-a-2d-matrix/description/
"""

"""
Tag: @BinarySearch
"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        i_l = 0
        i_r = len(matrix) - 1
        
        while (i_l < i_r - 1):
            mid = (i_l + i_r) / 2
            if (matrix[mid][0] < target):
                i_l = mid
            else:
                i_r = mid

        i_res = i_l if matrix[i_r][0] > target else i_r
        
        j_l = 0
        j_r = len(matrix[i_res]) - 1
        j_res = -1
        
        while (j_l <= j_r):
            mid = (j_l + j_r) / 2
            
            if (matrix[i_res][mid] == target):
                j_res = mid
                break
            if (matrix[i_res][mid] < target):
                j_l = mid + 1
            else:
                j_r = mid - 1
        
        return j_res != -1
        


matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

target = 11

sol = Solution()

sol.searchMatrix(matrix, target)

