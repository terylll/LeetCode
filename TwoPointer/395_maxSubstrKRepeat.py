from collections import defaultdict
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        max_len = 0

        for size in range(1, 27):
            m = {}          # Key: letter, Val: apperance
            begin = 0
            end = 0
            unique_letter = 0
            counter = 0     # Number of letters that satisfy the requirement

            while(end < len(s)):
                if (unique_letter <= size):
                    if (s[end] not in m or m[s[end]] == 0):
                        unique_letter += 1
                    
                    m[s[end]] = m[s[end]] + 1 if s[end] in m else 1

                    if (m[s[end]] == k):
                        counter += 1
                    
                    end += 1
                else:
                    # There are more unique letter in the window
                    if (m[s[begin]] == 1):
                        unique_letter -= 1

                    if (m[s[begin]] == k):
                        counter -= 1
                    
                    m[s[begin]] -= 1
                    
                    begin += 1

                if (unique_letter == size and counter == size):
                    # print(s[begin: end])
                    max_len = max(max_len, end - begin)
                
        return max_len
    
    def longestSubstring2(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        if (len(s) == 0):
            return 1

        count_map = {}
        
        for c in s:
            count_map[c] = count_map[c] + 1 if c in count_map else 1
        
        candidates = []
        idx = [1 for i in range(len(s))]

        # Remove invalid chars
        for i in range(len(s)):
            if (count_map[s[i]] < k):
                idx[i] = 0
        print(idx)

        for i in range(len(s)):
            if (i > 0 and idx[i] > 0 and idx[i - 1] > 0):
                idx[i] += idx[i - 1]
        print(idx)

        # Find max substring window
        end = idx.index(max(idx))
        begin = end

        while(begin > -1 and idx[begin] > 0):
            begin -= 1
        begin += 1

        return end - begin + 1
        

            

                

sol = Solution()
print(sol.longestSubstring2("ababacb", 3))

                    



    # def longestSubstring(self, s, k):
    #     """
    #     :type s: str
    #     :type k: int
    #     :rtype: int
    #     """
        
    #     m = {}          # Key: letter, Val: appearance
        

    #     counter = 0     # Number of unique letters that haven't meet the k repeat
    #     unique_letter = 0

    #     max_len = 0

    #     begin = 0
    #     end = 0
    #     while(end < len(s)):
    #         if (s[end] not in m or s[end] == 0):
    #             # New Character
    #             counter += 1
    #             unique_letter += 1

    #         m[s[end]] = m[s[end]] + 1 if s[end] in m else 1

    #         if (m[s[end]] >= k):
    #             counter -= 1
            
    #         end += 1

    #         # If there are at least one letter meet the requirement
    #         while(counter < unique_letter):
                
    #             # Maximize the range
    #             while(end < len(s) and s[end] in m and m[s[end]] > 0):
    #                 m[s[end]] += 1
    #                 end += 1
    #             print("!", s[begin: end])
    #             if (m[s[begin]] == 1):
    #                 # The last letter has been removed
    #                 unique_letter -= 1
    #             elif (m[s[begin]] == k):
    #                 # A new letter that doesn't meet the requirement
    #                 counter += 1
                
    #             m[s[begin]] -= 1

    #             begin += 1
            
    #             max_len = max(max_len, end - begin + 1)

    #     return max_len

            

            
        
