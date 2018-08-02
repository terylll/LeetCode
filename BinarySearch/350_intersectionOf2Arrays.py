class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        m = {}
        for num in nums1:
            if num not in m.keys():
                m[num] = 1
            else:
                m[num] += 1
        
        res = []
        for num in nums2:
            if num in m.keys() and m[num] > 0:
                res.append(num)
                m[num] -= 1
        
        return res

sol = Solution()
print(sol.intersect([], [1]))