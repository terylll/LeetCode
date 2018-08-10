class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """
        dp[i]           # Length of longest increasing subsequence up to dp[i]

        dp[i] = max(dp[m]) + 1 ( for m in 0 ... i - 1 and nums[m] < nums[i]
        """

        if (len(nums) == 0):
            return 0

        dp = [0 for i in nums]

        for i in range(len(nums)):
            cur_max = 0
            for j in range(i):
                if (nums[j] < nums[i]):
                    cur_max = max(cur_max, dp[j])
            
            dp[i] = cur_max + 1
        return max(dp)

sol = Solution()
print(sol.lengthOfLIS([1,3,6,7,9,4,10,5,6]))

        

