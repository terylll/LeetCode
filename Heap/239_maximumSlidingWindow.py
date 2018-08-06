from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        if (len(nums) == 0 or k <= 0):
            return [0]

        res = []

        q = deque()

        for i in range(len(nums)):
            # Remove elements that fall out of window of size k
            while(len(q) > 0 and q[0] < i - k + 1):
                q.popleft()
            
            while(len(q) > 0 and nums[q[-1]] < nums[i]):
                q.pop()
            
            q.append(i)
            
            if (i >= k - 1):
                res.append(q[0])

        return res

sol = Solution()
print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))