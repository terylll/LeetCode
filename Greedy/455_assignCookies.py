class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        
        if (len(g) == 0 or len(s) == 0):
            return 0


        g.sort()
        s.sort()

        count = 0

        i = 0 # index in g
        j = 0   # index in s
        
        while(i < len(g) and j < len(s)):
            if (g[i] <= s[j]):
                i += 1
                count += 1
            # g[i] > s[j]
            j += 1

        
        return count

sol = Solution()
print(sol.findContentChildren([1, 2, 3], [1, 1]))
