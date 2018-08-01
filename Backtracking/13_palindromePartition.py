class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        path = []
        res = []
        self.helper(s, 0, path, res)
        return res
    
    def helper(self, s, l, path, res):
        if (len(path) > 0 and l >= len(s)):
            res.append(list(path))
            return
        
        for i in range(l, len(s)):
            if (self.isPalindrome(s, l, i)):
                path.append(s[l:i+1])
                self.helper(s, i + 1,path, res)
                path.pop(-1)
        return

    def isPalindrome(self, s, l, r):
        while(l <= r):
            if (s[l] != s[r]):
                return False
            l += 1
            r -= 1
        return True

sol = Solution()
print(sol.partition("aab"))
            