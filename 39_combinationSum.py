class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        """
        Recursive Formula

        T(n) = (n - 1) * T(n - 1)
        T(1) = 1
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
        if (sum(path) > target):
            return
        
        if (sum(path) == target):
            res.append(path)
            return
        
        for i in range(start, len(candidates)):
            temp_path = [e for e in path]       # Create a new list and pass it to recursion call
            temp_path.append(candidates[i])
            self.bt(candidates, target, temp_path, res, i)
        
        return

sol = Solution()

print(sol.combinationSum([2,3,6,7], 7))