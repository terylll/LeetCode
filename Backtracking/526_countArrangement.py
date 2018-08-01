"""
Link: https://leetcode.com/problems/beautiful-arrangement/description/

Optimize

Memoization. Keep (pos, candidates) in cache to avoid unnecessary computation.

pos: position
candidates: rest of available numbers
"""

class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        used = [0 for i in range(N + 1)]
        res = [0]
        self.helper(N, used, [0], res)
        return res[0]

    def helper(self, N, used, path, res):
        
        if (len(path) - 1  >= N):
            # print(path)
            res[0] += 1
            return
        
        pos = len(path)
        for i in range(1, N + 1):
            # print("used[%d] = %d" % (i, used[i]))
            if (used[i] == 0 and (i % pos == 0 or pos % i == 0)):
                used[i] = 1
                path.append(i)
                # print("Path(+): %s" % path)
                self.helper(N, used, path, res)
                used[i] = 0
                path.pop(-1)
                # print("Path(-): %s" % path)
        return

sol = Solution()
print(sol.countArrangement(2))

            