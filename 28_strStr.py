class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if (needle == ""):
            return 0

        """
        Note: Edge Case
        """
        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if (needle[j] != haystack[i + j]):
                    break
                else:
                    if (j == len(needle) - 1):
                        return i
        
        return -1

sol = Solution()
print(sol.strStr("ab", "abc"))







"""
WRONG: CAN'T USE TWO POINTER
"""
# class Solution(object):
#     def strStr(self, haystack, needle):
#         """
#         :type haystack: str
#         :type needle: str
#         :rtype: int
#         """
        
#         if (needle == ""):
#             return 0
        
#         i = 0
#         j = 0
        
#         while (j < len(haystack)):
#             if (i == len(needle)):
#                 break
#             if (haystack[j] == needle[i]):
#                 i += 1
#             else:
#                 i = 0    
#             j += 1

#         if (i != len(needle)):
#             return -1
#         else:
#             return j - i