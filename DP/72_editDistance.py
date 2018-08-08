class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        if (len(word1) < len(word2)):
            return self.minDistance(word2, word1)
        
        
        dp = [[0 for i in range(len(word2) + 1)] for j in range(len(word1) + 1)]
        
        dp[0][0] = 0

        for j in range(len(word2) + 1):
            dp[0][j] = j
        
        for i in range(len(word1) + 1):
            dp[i][0] = i

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if (word1[i - 1] == word2[j - 1]):
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1] + 1, dp[i - 1][j] + 1, dp[i][j - 1] + 1)
        
        for row in dp:
            print(row)
        
        return dp[len(word1)][len(word2)]
        
sol = Solution()
print(sol.minDistance("sea", "eat"))