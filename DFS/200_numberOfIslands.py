class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (grid[i][j] == "1"):
                    # print(grid[i][j])
                    self.dfs(grid, i, j)
                    count += 1
        
        return count
    
    def dfs(self, grid, i, j):
        grid[i][j] = "0"
        
        if (i > 0 and grid[i - 1][j] == "1"):
            self.dfs(grid, i - 1, j)
        
        if (i < len(grid) - 1 and grid[i + 1][j] == "1"):
            self.dfs(grid, i + 1, j)
        
        if (j > 0 and grid[i][j - 1] == "1"):
            self.dfs(grid, i, j - 1)
        
        if (j < len(grid[i]) - 1 and grid[i][j + 1] == "1"):
            self.dfs(grid, i, j + 1)
        
        return

sol = Solution()
a = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print(sol.numIslands(a))