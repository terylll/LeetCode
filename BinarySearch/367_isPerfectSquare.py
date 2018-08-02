class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        l = 0
        r = num
        
        while (l < r):
            mid = (l + r) / 2
            # print(l, r, mid, num, num / mid)
            if (1.0 * num / mid > mid):
                l = mid + 1
            elif (1.0 * num / mid < mid):
                r = mid
            else:
                return True

        return False

sol = Solution()
print(sol.isPerfectSquare(1))
