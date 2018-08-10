class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """

        """

        buy[i][j]: At day 'j', the last action was buy. There are 'i' transaction till day 'j'
        sell[i][j]: At day 'i', the last action was sell    

        buy[i][j] = max{buy[i][j - 1], sell[i - 1][j - 1] - price[j]}
        sell[i][j] = max{sell[i][j - 1], buy[i][j - 1] + price[j]}

        Base Case:
        
        buy[0][0] = -price[0]
        """

        """
        Space down to O(n)

        buy[j] = max{buy[j - 1], prev_sell[j - 1] - price[j]}
        sell[j] = max{sell[j - 1], buy[j - 1] + price[j]}
        """

        """
        Key Observation:

        If k >= n/2, we can have transaction at any time
        """

        if (len(prices) == 0 or k == 0):
            return 0

        if (k >= len(prices) / 2):
            return self.buyStockAny(prices)

        buy = [0 for i in prices]
        sell = [0 for i in prices]
        prev_sell = [0 for i in prices]
        
        i = 0
        while i < k:
            buy[0] = -prices[0]
            for j in range(1, len(prices)):
                buy[j] = max(buy[j - 1], prev_sell[j - 1] - prices[j])
                sell[j] = max(sell[j - 1], buy[j - 1] + prices[j])
            temp = prev_sell
            prev_sell = sell
            sell = temp
            i += 1
        return prev_sell[len(prices) - 1]
    
    def buyStockAny(self, prices):
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit

sol = Solution()
array = [3,3,5,0,0,3,1,4]
print(sol.maxProfit(2, array))