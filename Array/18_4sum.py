class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        def nSum(nums, n, target, path, res):
            if n == 2:
                l = 0
                r = len(nums) - 1
                while (l < r):
                    s = nums[l] + nums[r]
                    if s == target:
                        res.append(path + [nums[l], nums[r]])
                        l += 1
                        # Remove Duplicate
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(len(nums) - n + 1):
                    if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                        nSum(nums[i + 1:], n - 1, target - nums[i], path + [nums[i]], res)
        
        res = []
        nums.sort()
        nSum(nums, 4, target, [], res)
        return res

sol = Solution()
print(sol.fourSum([1, 0, -1, 0, -2, 2], 0))