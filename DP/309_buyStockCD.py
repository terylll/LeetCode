class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        d = [0 for i in range(len(prices))]
        
        for i in range(1, len(prices)):
            # Check cd
            if (i > 3 and d[i - 3] < d[i - 2] and d[i - 2]== d[i - 1]):
                d[i] = d[i - 1]
            else:
                d[i] = max(d[i - 1] + prices[i] - prices[i - 1], d[i - 1])
        
        return d[len(prices) - 1]

sol = Solution()
print(sol.maxProfit([1,2,3,0,2]))