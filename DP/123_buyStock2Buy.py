class Solution(object):
    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        """
        O(n^3): TLE
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

    def maxProfit(self, prices):
        """

        buy[i][j]: At day 'j', the last action was buy. There are 'i' transaction till day 'j'
        sell[i][j]: At day 'i', the last action was sell    

        buy[i][j] = max{buy[i][j - 1], sell[i - 1][j - 1] - price[j]}
        sell[i][j] = max{sell[i][j - 1], buy[i][j - 1] + price[j]}

        Base Case:
        
        buy[0][0] = -price[0]
        """

        buy = [[0 for j in prices] for i in range(2)]
        sell = [[0 for j in prices] for i in range(2)]

        buy[0][0] = -prices[0]
        buy[1][0] = -prices[0]

        for i in range(2):
            for j in range(1, len(prices)):
                buy[i][j] = max(buy[i][j - 1], sell[i - 1][j - 1] - prices[j])
                sell[i][j] = max(sell[i][j - 1], buy[i][j - 1] + prices[j])
        return max(sell[0][-1], sell[1][-1])

sol = Solution()
print(sol.maxProfit([7, 6, 5, 4, 3, 2, 1]))