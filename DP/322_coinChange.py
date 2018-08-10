class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        """
        dp[i] = min(dp[i - 5], dp[i - 2], dp[i - 1]) + 1

        # Base Case
        dp[given] = 1
        """


        if (len(coins) == 0):
            return - 1
        
        if (amount == 0):
            return 0

        dp = [float('inf') for i in range(amount + 1)]

        for c in coins:
            if (c <= amount):
                dp[c] = 1
        # print(dp)
        for i in range(1, amount + 1):
            if (dp[i] == 1):
                continue
            
            cur_min = float('inf')
            for coin in coins:
                if (i - coin > 0):
                    cur_min = min(cur_min, dp[i - coin])
            
            dp[i] = cur_min + 1 if cur_min != float('inf') else cur_min
            # print(dp)
        
        return dp[amount] if dp[amount] != float('inf') else -1

sol = Solution()
print(sol.coinChange([1], 0))



