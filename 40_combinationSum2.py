class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        candidates.sort()
        res = []
        p = []

        self.bt(candidates, target, p, res, 0)

        return res
        
    def bt(self, candidates, target, path, res, start):
        """
        Parameters
            candidates      List of candidate numbers   
            target          Target value
            path            
            res             List that stores solution
            start           Index of next element to be added
        """

        # Base Case
        if (sum(path) > target or start >= len(candidates)):
            return
        
        if (sum(path) == target):
            # print("[Found]Path = %s, start = %s" % (path, start))
            res.append(path)
            return
        
        for i in range(start, len(candidates)):
            if (i > start and candidates[i] == candidates[i - 1]):
                continue
            temp_path = [e for e in path]       # Create a new list and pass it to recursion call
            temp_path.append(candidates[i])
            # print("start = %d, i = %d, path = %s" % (start, i, temp_path))
            self.bt(candidates, target, temp_path, res, i + 1)

        return

sol = Solution()
print(sol.combinationSum2([10,1,2,7,6,1,5], 8))
