class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        dp = [0 for i in nums]
        
        if (len(nums) == 0):
            return 0
        
        if (len(nums) == 1):
            return nums[0]
        
        if (len(nums) == 2):
            return nums[1]
        
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        
        print(dp)

        return dp[-1]

sol = Solution()
print(sol.rob([1,2,3,1]))