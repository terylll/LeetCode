class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        
        """
        Key Obs:
            If s1 [0 ... i] and s2 [0 ... j] is interleaving, dp[i][j] points to s3[i + j]
        
        If s1[i] == s3[i + j]:
            dp[i][j] = dp[i - 1][j]
        elif s2[j] == s3[i + j]:
            dp[i][j] = dp[i][j - 1]
        
        Base Case
        dp[0][0]  = True
        """

        if (len(s1) == 0 and len(s2) == 0):
            return False
        
        if (len(s1) == 0 and len(s2) == 0 and len(s3) == 0):
            return True
        
        # if (len(s1) + len(s2) != len(s3)):
        #     return False
        
        dp = [[False for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
        
        dp[0][0] = True
        
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if (i == 0 and j == 0):
                    dp[i][j] = True
                elif (0 <= i - 1 < len(s1 ) and 0 <= i + j - 1 < len(s3) and s1[i - 1] == s3[i + j - 1]):
                    if (j == 0):
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i - 1][j]
                elif (0 <= j - 1 < len(s2) and 0 <= i + j - 1 < len(s3) and s2[j - 1] == s3[i + j - 1]):
                    if (i == 0):
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i][j - 1]

        return dp[len(s1)][len(s2)]

sol = Solution()
print(sol.isInterleave("a", "b", "a"))