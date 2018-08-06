class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        """
        buy[i]: Buy stock at day 'i'. The profit.

        sell[i]: Sell stock at day 'i'. The profit.

        Recursion Formula

        buy[i] = max( sell[i - 2] - prices[i], buy[i - 1])  # Buy or not buy

        sell[i] = max( buy[i - 1] + price[i], sell[i - 1]) # Sell or not sell

        TODO: Why 'buy[i - 1]' ?
        """

        """
        buy[i]: At day 'i', last action was buy. Profit.
        sell[i]: At day 'i', last action was sell.

        1) CD 1 day. Buy & Sell - 1d
        2) buy before sell
        3) max(sell[i], buy[i], rest[i]) = sell[i] 

        buy[i] = max(sell[i - 2] - price[i], buy[i - 1])
        sell[i] = max(buy[i - 1] + price[i], sell[i - 1])


        #Base Case
        buy[0] = 0 - price[0]

        1 ... n

        """

        buy = [0 for i in prices]
        sell = [0 for i in prices]

        buy[0] = 0 - prices[0]
        sell[0] = 0
        
        for i in range(1, len(prices)):
            buy[i] = max(sell[i - 2] - prices[i], buy[i - 1])
            if (i > 0):
                sell[i] = max(buy[i - 1] + prices[i], sell[i - 1])
            print(buy, sell)
        return sell[-1]


sol = Solution()
print(sol.maxProfit([1,2,3,0,2]))