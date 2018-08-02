class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        l = 0
        r = len(nums) - 1
        n = len(nums)

        while (l < r):
            
            mid = (l + r) / 2

            print(l, r, mid)
            
            if (nums[mid] > nums[r]):
                l = mid + 1
            else:
                # nums[mid] <= nums[r]
                r = mid 
                
        return nums[l]

sol = Solution()
print(sol.findMin([3,1,2]))

        