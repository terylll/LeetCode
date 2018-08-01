"""
Link: https://leetcode.com/problems/combination-sum-iii/description/
"""

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        used = [0 for i in range(10)]
        res = []
        self.helper(k, n, used, 0, [], res)
        return res

    def helper(self, K, N, used, pos, path, res):
        if (len(path) >= K):
            if (sum(path) == N):
                res.append(list(path))
                # res.append(path)
            return

        for i in range(1, 10):
            if (used[i] == 0):
                if (sum(path) + i > N or i < pos):
                    continue
                used[i] = 1
                path.append(i)
                self.helper(K, N, used, i, path, res)
                used[i] = 0
                path.pop(-1)
        return

sol = Solution()
print(sol.combinationSum3(3, 7))

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        