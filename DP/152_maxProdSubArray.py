class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        """
        dp[i]: The product of maximum sub array in nums[0 ... i] such that the last element is nums[i]

        Keep track of max_so_far and min_so_far because of product.
        """


        if(len(nums) == 0):
            return 0
        
        if(len(nums) == 1):
            return nums[0]

        global_max = nums[0]
        cur_max = nums[0]
        cur_min = nums[0]

        for i in range(1, len(nums)):
            candidates = [cur_max * nums[i], cur_min * nums[i], nums[i]]
            cur_max = max(candidates)
            cur_min = min(candidates)
            global_max = max(global_max, cur_max)
        
        return global_max

sol = Solution()
print(sol.maxProduct([-2, 3, -4]))
