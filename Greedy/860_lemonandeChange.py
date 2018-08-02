class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        
        five = 0
        ten = 0
        for i in bills:
            if i == 5:
                five += 1
            elif i == 10:
                five -= 1
                ten += 1
            elif i == 20:
                if (ten < 1):
                    five -= 3
                else:
                    five -= 1
                    ten -= 1
            if five < 0 or ten < 0:
                return False
        return True
        
sol = Solution()
print(sol.lemonadeChange([5,5,10,10, 20]))