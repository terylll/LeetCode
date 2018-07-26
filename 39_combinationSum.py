class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        path = []
        self.dfs(candidates, path, target, res)
        print("Final Result: ", res, path)
        return
        
    
    def dfs(self, candidates, path, target, res):
        """
        :param candidates: List of candidates
        :param path: List of selected number
        :param target: numbers to get
        """

        print("*" * 30)
        print("Candidates: ", candidates)
        print("Path: ", path)
        print("Target: ", target)
        print("Res: ", res)

        if (target < 0):
            return

        if (target == 0):
            res.append(path)
            return
        
        number = candidates.pop()
        
        # Add number
        path.append(number)
        self.dfs(candidates, path, target - number, res)

        # Don't add number
        self.dfs(candidates, path, target, res)

sol = Solution()
sol.combinationSum([2, 3, 6, 7], 7)


