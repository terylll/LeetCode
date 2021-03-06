class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        
        # Move back to front

        i = m - 1
        j = n - 1
        
        p = m + n - 1
        while(j >= 0):
            if (i >= 0 and nums1[i] > nums2[j]):
                nums1[p] = nums1[i]
                i -= 1
            else:
                nums1[p] = nums2[j]
                j -= 1

            p -= 1
        
        # return nums1

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
sol = Solution()
sol.merge(nums1, 3, nums2, 3)
print(nums1)