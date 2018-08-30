class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ""
        while(n > 0):
            
            print(dif)
            res += chr(ord("A") + dif - 1)
            n -= dif
        print(res)

sol = Solution()
sol.convertToTitle(27)
            