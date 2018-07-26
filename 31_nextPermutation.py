"""
Link: https://leetcode.com/problems/next-permutation/description/
"""

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # Edge Case
        if (len(nums) < 2):
            return


        p = -1
        # Rerverse
        for i in range(len(nums) - 2, -1, -1):
            if (nums[i] < nums[i + 1]):
              p = i
              break
        if (p != -1):
            # Find swap
            q = p + 1
            for i in range(p + 1, len(nums)):  
                if (nums[i] > nums[p]):
                    q = i

            # Swap
            t = nums[p]
            nums[p] = nums[q]
            nums[q] = t
            # print nums

            # Reverse nums[p + 1 ....]
            i = p + 1
            j = len(nums) - 1
            while (i < j):
                t = nums[i]
                nums[i] = nums[j]
                nums[j] = t
                i += 1
                j -= 1
        else:
            i = 0
            j = len(nums) - 1
            while (i < j):
                t = nums[i]
                nums[i] = nums[j]
                nums[j] = t
                i += 1
                j -= 1

sol = Solution()
nums = [1, 3, 2]
sol.nextPermutation(nums)
print nums