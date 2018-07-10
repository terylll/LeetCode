"""
Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
"""


"""
Using stack. FIFO.
"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        res = []

        if (len(digits) == 0):
            return res

        
        
        mapping = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        
        res.append("")

        for i in range(len(digits)):
            while(len(res[0]) == i):

                e = res.pop(0)
                for c in mapping[int(digits[i])]:
                    res.append(e + c)
                    # print(c, e + c)
        return res

sol = Solution()
print(sol.letterCombinations("23"))
        
    