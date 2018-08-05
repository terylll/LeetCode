"""
Link: https://leetcode.com/problems/longest-palindromic-substring/description/
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # Build matrix
        res = []
        for i in range(len(s)):
            res.append([])
            for j in range(len(s)):
                res[i].append(0)
        
        """
        Base case
        1) r[i] == r[i]
        2) r[i] == r[i + 1]
        """

        for i in range(len(s)):
            res[i][i] = 1
        
        for i in range(len(s) - 1):
            if (s[i] == s[i + 1]):
                res[i][i + 1] = 1
        
        """
        DP
        r[i][j]: s[i ... j] is a palindrome

        r[i][j] = r[i + 1][j - 1] if (s[i] == s[j]) 
        """
        for offset in range(2, len(s)):
            for i in range(len(s) - offset):
                if (res[i + 1][i + offset - 1] == 1 and s[i] == s[i + offset]):
                    res[i][i + offset] = 1
        
        """
        Find Longest
        """
        maxLen = -1
        ans = ""
        for i in range(len(res)):
            for j in range(i, len(res[i])):
                if (res[i][j] == 1 and abs(i - j) > maxLen):
                    maxLen = abs(i - j)
                    ans = s[i:j + 1]
        return ans

sol = Solution()
print sol.longestPalindrome("")