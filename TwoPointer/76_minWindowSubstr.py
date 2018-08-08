import sys
# from collections import defaultdict
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        counter = 0
        m = {}
        
        # Fill the map
        for c in t:
            if (c in m):
                m[c] += 1
            else:
                m[c] = 1
        
        counter = len(t)

        min_window = float('inf')
        cur_window = 0
        min_head = 0
        begin = 0
        end = 0
        
        # Begin Search
        while(end < len(s)):
            if (s[end] in m.keys()):
                if (m[s[end]] > 0):
                    counter -= 1
                m[s[end]] -= 1
            end += 1

            # Find min window if all char in t are found
            while(counter == 0):
                cur_window = end - begin
                if (cur_window < min_window):
                    min_window = cur_window
                    min_head = begin

                if (s[begin] in m):
                    m[s[begin]] += 1
                    if (m[s[begin]] > 0):
                        counter += 1
                begin += 1
        return s[min_head: min_head + min_window] if min_window != float('inf') else ""

sol = Solution()
print(sol.minWindow("ADOBECODEBANC", "ABC"))

            

