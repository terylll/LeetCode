class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        
        """
        dp[i][j] = min(dp[i - 1][j - 1] + val[i][j], dp[i - 1][j] + val[i][j])
        """

        prev = [0 for i in range(len(triangle))]
        dp = [0 for i in range(len(triangle))]

        for i in range(len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    dp[j] = prev[j] + triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    dp[j] = prev[j - 1] + triangle[i][j]
                else:
                    dp[j] = min(prev[j - 1] + triangle[i][j], prev[j] + triangle[i][j])

            dummy = prev
            prev = dp
            dp = dummy

        return min(prev)


t = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
sol = Solution()
print(sol.minimumTotal(t))