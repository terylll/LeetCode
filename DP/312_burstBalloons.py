class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Add padding
        val = [1]
        for i in nums:
            val.append(i)
        val.append(1)

        dp = [[0 for j in range(len(nums) + 2)] for i in range(len(nums) + 2)]

        for l in range(1, len(nums) + 1):
            for i in range(1, len(nums) + 2 - l):
                j = i + l - 1
                for k in range(i, j + 1):
                    dp[i][j] = max(dp[i][j], dp[i][k - 1] + val[i - 1] * val[k] * val[j + 1] + dp[k + 1][j])
    
        return dp[1][len(nums)]

sol = Solution()
print(sol.maxCoins([3,1,5,8]))