class Solution(object):
    """
    dp[i][j]: Number of matched substring s[:i] with t[:j] such that the last letter is s[i] and t[j]

    for j in 0 .... t:
        if s[i] == t[j]:
            dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i - 1][j])        # Match or No match
        else:
            dp[i][j] = dp[i - 1][j]
    """
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """

        dp = [[0 for j in range(len(t) + 1)] for i in range(len(s) + 1)]

        # "" is the substring of all strings
        for i in range(len(dp)):
            dp[i][0] = 1
        
        for j in range(len(t)):
            for i in range(len(s)):
                if (s[i] == t[j]):
                    dp[i + 1][j + 1] = dp[i][j] + dp[i][j + 1]
                else:
                    dp[i + 1][j + 1] = dp[i][j + 1]
            # print(t[j], dp)
        
        return dp[len(s)][len(t)]
        

sol = Solution()
print(sol.numDistinct("babgbag", "bag"))
        