class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        dp = [[0 for j in s] for i in s]

        max_len = 1
        
        # Base Case
        for i in range(len(s)):
            dp[i][i] = 1
        
        for i in range(1, len(s)):
            if (s[i] == s[i - 1]):
                max_len = 2
                dp[i - 1][i] = 2
        
        for d in range(2, len(s)):
            i = len(s) - d - 1
            while i >= 0:
                j = i + d
                if (s[i] == s[j]):
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
                
                i -= 1
                    
                    
        
        return dp[0][len(s) - 1]

sol = Solution()
print(sol.longestPalindromeSubseq("bbbab"))