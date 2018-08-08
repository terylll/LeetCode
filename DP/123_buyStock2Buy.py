class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        """
        p[i][j]: The most profit that i-th transaction until day 'j'.

        TODO: Not ends at day 'j'.

        p[i][j] = max(p[i][j - 1], 
                        max( p[i - 1][jj] + val[j] - val[jj]) for jj in 0 ... j - 1
        """

        """
        Base Case
        p[0][j] = 0     # 0 transaction -> 0 profit
        p[i][0] = 0     
        """

        p =[[0 for j in prices] for i in range(3)]

        for i in range(1, 3):
            for j in range(len(prices)):
                for k in range(0, j):
                    p[i][j] = max(p[i][j], p[i - 1][k] + prices[j] - prices[k])
                p[i][j] = max(p[i][j], p[i][j - 1])
        return p[2][len(prices) - 1]

sol = Solution()
print(sol.maxProfit([1, 2, 3, 4, 5]))