class Solution(object):
    """
    Naive Backtracking
    """
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        """
        memo: A memoization map

        Key: substring s
        Value: The words that is in the substring
        """
        
        memo = {}
        path = []
        res = []
        ans = self.bt(0, s, wordDict, memo)
        return [' '.join(i) for i in ans]
   
    def dfs(self, start, s, wordDict, memo):
        if (s[start:] in memo):
            return memo[s[start:]]

        res = []
        if (start == len(s)):
            res.append([])
            return res
        
        for i in range(start + 1, len(s) + 1):
            word = s[start: i]
            if (word in wordDict):
                sublist = self.dfs(i, s, wordDict, memo)
                for sub in sublist:
                    res.append([word] + sub)
        
        memo[s[start:]] = res

        return res



sol = Solution()
print(sol.wordBreak("catsanddog", ["cats", "dog", "sand", "and", "cat"]))