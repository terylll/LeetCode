"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

- You must do this in-place without making a copy of the array.
- Minimize the total number of operations.
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        # Slow-Fast Pointer

        zeroIdx = 0

        """
        TODO: Handle edge case
        case:   [1]
        sol:    Check index validity first then check value. Otherwise IndexError
        """
        while (zeroIdx < len(nums) and nums[zeroIdx] != 0):
            zeroIdx += 1

        for i in range(zeroIdx + 1, len(nums)):
            if (nums[i] != 0):
                # Swap
                temp = nums[i]
                nums[i] = nums[zeroIdx]
                nums[zeroIdx] = temp

                # Increase zero index
                while (nums[zeroIdx] != 0 and zeroIdx < i):
                    zeroIdx += 1
        

if __name__ == '__main__':
    sol = Solution()
    a = [1, 3, 12, 0]
    sol.moveZeroes(a)
    print a
    
        