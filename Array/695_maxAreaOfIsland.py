class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        """
        	Time Complexity: O(n^2)
        	Space Complexity: O(n)
        """


        maxArea = 0
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j):

        	"""
        		Check boundary first then check value
        	"""
        	if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
        		grid[i][j] = 0
        		return 1 + dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1)
        	return 0

        """
        	Corner case:
        		if grid[i][j] are all 0, ares will be null. Check areas first before return.
        """	
        areas = [dfs(i, j) for i in range(m) for j in range(n) if grid[i][j]]
        return max(areas) if areas else 0
        