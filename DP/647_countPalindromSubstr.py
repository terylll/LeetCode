class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        """
        dp[i][j]:   Whether or not substring s[i ... j] is a palindrome
        
        if s[i] == s[j]:
            dp[i][j] = dp[i + 1][j - 1]
        else:
            dp[i][j] = False
        
        Base Case:

        dp[i][i] = True
        """

        count = 0
        dp = [[False for j in s] for i in s]

        # Base Case
        for i in range(len(s)):
            dp[i][i] = True
            count += 1
        
        for i in range(1, len(s)):
            if (s[i] == s[i - 1]):
                dp[i - 1][i] = True
                count += 1
        # DP

        for d in range(2, len(s) + 1):
            for i in range(len(s) - d):
                j = i + d
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                    if (dp[i][j] == True):
                        count += 1
                else:
                    dp[i][j] = False
        
        return count

sol = Solution()
print(sol.countSubstrings("aaa"))

