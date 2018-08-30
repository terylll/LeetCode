class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        return [i for i in s.lstrip(" ").rstrip(" ").split(" ") if len(i) != 0].reverse()