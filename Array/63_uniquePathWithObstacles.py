class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        
        res = []
        for i in range(len(obstacleGrid)):
            res.append([])
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    res[i].append(0)
                else:
                    if i != 0 and j != 0:
                        res[i].append(res[i][j - 1] + res[i-1][j])
                    elif i == 0 and j == 0:
                        res[i].append(1)
                    elif i == 0:
                        res[i].append(res[i][j - 1])
                    elif j == 0:
                        res[i].append(res[i-1][j])
        return res[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1]
                
                