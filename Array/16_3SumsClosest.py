"""
Link: https://leetcode.com/problems/3sum-closest/description/
"""

class Solution(object):
    def threeSumClosest(self, n, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(n)
        
        globalMin = float('inf')
        res = [-1, -1, -1]
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            print (i,j,k)
            while (j < k):
                ## Check Min
                if (abs(nums[i] + nums[j] + nums[k] - target) < globalMin):
                    globalMin = abs(nums[i] + nums[j] + nums[k] - target)
                    res[0] = i
                    res[1] = j
                    res[2] = k
                
                ## Check direction
                if (nums[i] + nums[j] + nums[k] > target):
                    k -= 1
                else:
                    j += 1
                    
        return sum([nums[i] for i in res])


sol = Solution()
print sol.threeSumClosest([-1, 2, 1, -4], 1)