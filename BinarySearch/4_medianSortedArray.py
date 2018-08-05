class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        m = len(nums1)
        n = len(nums2)
        
        # Make sure m < n
        if (m > n):
            return self.findMedianSortedArrays(nums2, nums1)

        i_l = 0
        i_r = m
        while (i_l <= i_r):
            i_mid = (i_l + i_r) / 2
            j = (m + n) / 2 - i_mid
            print(i_l, i_r, i_mid, j)
            if (nums2[j - 1] < nums1[i_mid]):
                i_l = i_mid + 1
            elif (nums2[j - 1] > nums1[i_mid]):
                i_r = i_mid - 1
            else:
                maxLeft = max(nums1[i_mid - 1], nums2[j - 1])
                minRight = min(nums1[i_mid], nums2[j])
                print(maxLeft, minRight)
                if (m + n) % 2 == 0:
                    return minRight
                else:
                    return (maxLeft + minRight) / 2
        return 0

sol = Solution()
print(sol.findMedianSortedArrays([1, 3], [2, 4])) 

        