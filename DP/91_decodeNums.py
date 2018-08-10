class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        """
        dp[i]: Number of ways to decode the string s[0 ... i]

        if s[i] is valid:
            if s[i - 1: i] is valid:
                dp[i] = dp[i - 1] + dp[i - 2]
            else:
                dp[i] = dp[i - 1]
        else:
            if s[i - 1: i] is valid:
                dp[i] = dp[i - 2]
        
        Base Case:
            s[0] = 1
        """

        if (len(s) == 0):
            return 0

        # Padding
        s = "0" + s

        dp = [0 for i in s]
        dp[0] = 1

        for i in range(1, len(s)):
            if 1 <= int(s[i]) <= 9:
                dp[i] += dp[i - 1]
            if 10 <= int(s[i - 1: i + 1]) <= 26:
                dp[i] += dp[i - 2]
        
        return dp[len(s)]

        

