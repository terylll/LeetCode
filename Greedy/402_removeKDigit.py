class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        
        stack = [];
        
        for c in num:
            d = int(c);
            while (k > 0 and len(stack) > 0 and stack[-1] > d):
                stack.pop()
                k -= 1
            stack.append(d)
        
        while(k > 0):
            stack.pop()
            k -= 1

        res = ""
        while(len(stack) != 0):
            res += str(stack.pop())
        res = res[::-1].lstrip('0')

        if (len(res) == 0):
            res = "0"
        return res
        
sol = Solution()
print(sol.removeKdigits("1230", 3))
