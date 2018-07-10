"""
Link: https://leetcode.com/problems/generate-parentheses/description/
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []

        def bt(s, left, right):
            if (len(s) == n * 2):
                res.append(s)
                return
            if (left < n):
                bt(s + "(", left + 1, right)
            if (right < left):
                bt(s + ")", left, right + 1)
        
        bt("", 0, 0)

        return res

sol = Solution()
print sol.generateParenthesis(2)

        
