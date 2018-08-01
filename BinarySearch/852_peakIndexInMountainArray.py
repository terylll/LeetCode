class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        l = 0
        r = len(A) - 1
        while (l < r):
            mid = (l + r) / 2
            if (A[mid] < A[mid + 1]):
                l = mid + 1
            else:
                r = mid
        return l


sol = Solution()
print(sol.peakIndexInMountainArray([0,1,2,3]))