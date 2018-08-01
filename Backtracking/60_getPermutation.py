class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        used = [0 for i in range(n + 1)]
        path = []
        res = []
        self.helper(n, k, used, path, res)
        return "".join([str(i) for i in res[k - 1]])
        

    def helper(self, n, k, used, path, res):
        if (len(res) == k):
            return True
        if (len(path) == n):
            res.append(list(path))
            
        
        for i in range(1, n + 1):
            if (used[i] == 0):
                used[i] = 1
                path.append(i)
                if (self.helper(n, k, used, path, res) is True):
                    return True
                used[i] = 0
                path.pop(-1)
        
        return False

sol = Solution()
print(sol.getPermutation(9, 273815))
        