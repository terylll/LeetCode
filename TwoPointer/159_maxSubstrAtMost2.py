class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        m = {}      # Key: char Value: # of appearance in the window

        counter = 0 # Number of unique letters in the window

        begin = 0
        end = 0

        max_len = 0

        while (end < len(s)):
            if (s[end] not in m or m[s[end]] == 0):
                counter += 1
            
            m[s[end]] = m[s[end]] + 1 if s[end] in m else 1

            end += 1
            
            while (counter > 2):
                m[s[begin]] -= 1
                if (m[s[begin]] == 0):
                    counter -= 1
                begin += 1
            
            max_len = max(max_len, end - begin)
        
        return max_len

            

            