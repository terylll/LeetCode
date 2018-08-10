class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        """
        dp[i][j]: The result if player one choose 'i' or 'j'

        if player one choose 'i':
            dp[i][j] = val[i] + min(val[i + 1], val[j])     # Player 2 will choose max(val[i + 1], val[j - 1])
        
        if plyaer one choose 'j':   
            dp[i]j] = val[j]  + min(val[i], val[j - 1])     # Player 2 will choose max(val[i + 1], val[j - 1])                          
        
        dp[i][j] = max((1), (2))

        #Base Case:

        if (len(nums) % 2 == 1):
            dp[i][i] = val[i]
        else:
            dp[i][i] = 0
            dp[i][i - 1] = max(val[i], val[i - 1])

        # Recur
        for d in range(len(d) - 1, -1, -2)
        """

        dp = [[0 for j in nums] for i in nums]

        if (len(nums) % 2 == 0):
            for i in range(1, len(nums)):
                dp[i][i - 1]= max(nums[i], nums[i - 1])
        else:
            for i in range(len(nums)):
                dp[i][i] = nums[i]
        # Recur
        d = 3 if (len(nums) % 2 == 0) else 2
        while(d < len(nums)):
            for i in range(len(nums) - d):
                j = i + d
                choose_i = 0
                choose_j = 0
                if (nums[i + 1] < nums[j]):
                    choose_i = dp[i + 1][j - 1] + nums[i]
                else:
                    choose_i = dp[i + 2][j] + nums[i]
                
                if (nums[i] < nums[j - 1]):
                    choose_j = dp[i][j - 2] + nums[j]
                else:
                    choose_j = dp[i + 1][j - 1] + nums[j]
                
                dp[i][j] = max(choose_i, choose_j)
            d += 2
            # print(d, dp)
        print(dp[0][len(nums) - 1])
        return dp[0][len(nums) - 1] > (sum(nums) / 2)

sol = Solution()
print(sol.PredictTheWinner([1, 5, 233, 7]))

