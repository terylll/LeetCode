class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        res = 0

        sorted(nums)

        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while(j < k):
                if (nums[i] + nums[j] + nums[k] < target):
                    """
                    If a[i] + a[j] + a[k] < target, a[i] < a[j] < a[k],
                    then for all p in j ... k, a[i] + a[j] + a[p] < target
                    """
                    # Moving k backward
                    res += k - j
                    j += 1
                else:
                    k -= 1
        return res

sol = Solution()
print(sol.threeSumSmaller([3,1,0,-2], 4))