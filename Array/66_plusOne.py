class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        digits[len(digits) - 1] += 1
        
        add = 0
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += add
            add = digits[i] / 10
            digits[i] %= 10
        
        if add != 0:
            digits = [add] + digits
        
        return digits