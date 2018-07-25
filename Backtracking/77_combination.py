class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        res = []

        nums = range(1, n + 1)

        self.bt(nums,[], 0, k, res)
        
        return res

    
    def bt(self, nums, path, start, k, res):
        """

        """

        if (len(path) == k):
            res.append(path)
            return
        
        for i in range(start, len(nums)):
            temp_path = [e for e in path]
            temp_path.append(nums[i])
            self.bt(nums,temp_path, i + 1, k, res)
        
        return

sol = Solution()
print(sol.combine(4, 2))
        


