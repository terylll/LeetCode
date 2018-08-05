class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        """
        dp[i]: The sub string s[:i] can form a word break. There is a word in s[:i] such that the last char is s[i].

        Time: O(n^2)
        """
        
        dp = [False for i in s]

        for i in range(len(s)):
            for word in wordDict:
                if (word == s[i - len(word) + 1:i + 1] and (dp[i - len(word)] is True or i - len(word) == -1)):
                    dp[i] = True
                    break
        
        return dp[-1]

sol = Solution()
print(sol.wordBreak("leetcode", ["leet", "code"]))
