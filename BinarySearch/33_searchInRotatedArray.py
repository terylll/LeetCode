class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        l = 0
        r = len(nums) - 1
        n = len(nums)

        while (l < r):
            mid = (l + r) / 2
            if (nums[mid] > nums[r]):
                l = mid + 1
            else:
                # nums[mid] <= nums[r]
                r = mid
        

        offset = l
        l = 0
        r = len(nums) - 1
        while(l <= r):
            mid = (l + r) / 2
            realmid = (mid + offset) % n
            # print(l, r, mid, realmid)
            if (nums[realmid] == target):
                return realmid
            elif (nums[realmid] < target):
                l = mid + 1
            else:
                r = mid - 1
        return -1

sol = Solution()
print(sol.search([4,5,6,7,0,1,2], 3))
