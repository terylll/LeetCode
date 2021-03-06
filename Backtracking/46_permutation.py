class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        ans = []

        nums.sort()

        used = [False for i in nums]

        self.bt(nums, used, [], ans)
        return ans

    def bt(self, nums, used, path, res):
        # Base Case
        if (len(path) == len(nums)):
            res.append(path)
            return
        
        for i in range(len(nums)):
            if used[i] :
                continue
            
            used[i] = True
            temp_path = [e for e in path]
            temp_path.append(nums[i])
            self.bt(nums, used, temp_path, res)
            used[i] = False
        
        return
    
sol = Solution()
print(sol.permute([1,1,2]))