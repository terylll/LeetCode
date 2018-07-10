"""
Link: https://leetcode.com/problems/3sum/description/
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        print (nums)
        res = []
        for i in range(len(nums) - 2):
            if (nums[i] == 0 or nums[i] != nums[i - 1]):        ## Explore Combiantion earliest
                low = i + 1
                high = len(nums) - 1
                target = 0 - nums[i]
                while (low < high):
                    if (nums[low] + nums[high] == target):
                        pair = [nums[i], nums[low], nums[high]]
                        res.append(pair)
                        while(low < high and nums[low] == nums[low + 1]):
                            low += 1
                        while(low < high and nums[high] == nums[high - 1]):
                            high -=1
                        low += 1
                        high -= 1
                    elif (nums[low] + nums[high] < target):
                        low += 1
                    else:
                        high -= 1
        
        return res

sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))
                
                