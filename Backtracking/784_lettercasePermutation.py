class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = []
        self.helper(S, 0, "", res)
        return res

    def helper(self, S, start, path, res):
        if (start >= len(S)):
            res.append(path)
            return
        
        if (not S[start].isalpha()):
            self.helper(S, start + 1, path + S[start], res)
        else:
            self.helper(S, start + 1, path + S[start].lower(), res)
            self.helper(S, start + 1, path + S[start].upper(), res)

        return
        

    # def bt(self, S, start, path, res):
    #     if (start >= len(S)):
    #         s = ''.join(path)
    #         res.append(s)
    #         return
        
    #     x = S[start]
    #     if (x.isalpha()):
    #         candidates = [x]
    #         candidates.append(x.upper() if x.islower() else x.lower())
    #         for i in range(len(candidates)):
    #             temp_path = [e for e in path]
    #             temp_path.append(candidates[i])
    #             self.bt(S, start + 1, temp_path, res)
    #     else:
    #         temp_path = [e for e in path]
    #         temp_path.append(x)
    #         self.bt(S, start + 1, temp_path, res)
    #     return

sol = Solution()
print(sol.letterCasePermutation(""))
                
        






