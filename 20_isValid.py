class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        valid = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        
        stack = []
        
        flag = False
        
        for i in s:
            if valid.has_key(i):
                stack.append(i)
            else:
                if (len(stack) == 0 or valid[stack.pop()] != i):
                    return False
        
        if (len(stack) == 0):
            return True
        else:
            return False

sol = Solution()
print sol.isValid("]")
