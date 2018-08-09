class NumArray(object):

    # O(n)
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.dp = []

        for i in range(len(nums)):
            if i == 0:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i - 1] + nums[i]
        
        self.dp.append(0)
        
        

    # O(1) Query
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return dp[j] - dp[i - 1]
    
    
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)