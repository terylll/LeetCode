class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """

        # Compare with top-left neighbor
        for i in range(len(matrix)):
        	for j in range(len(matrix[i])):
        		if i == 0 or j == 0 or matrix[i][j] == matrix[i-1][j-1]:
        			continue
        		else:
        			return False
       	return True