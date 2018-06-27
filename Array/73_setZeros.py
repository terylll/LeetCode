class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        col_0 = 1
        # Search
        for i in range(len(matrix)):
            if (matrix[i][0] == 0):
                col_0 = 0
            for j in range(1, len(matrix[0])):
                if (matrix[i][j] == 0):
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        print(matrix)

        for i in range(len(matrix) - 1, -1, -1):
            for j in range(len(matrix[0]) - 1, 0, -1):
                if (matrix[0][j] == 0 or matrix[i][0] == 0):
                    matrix[i][j] = 0
            if (col_0 == 0):
                matrix[i][0] = 0
        
        

sol = Solution()
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
sol.setZeroes(matrix)
print(matrix)