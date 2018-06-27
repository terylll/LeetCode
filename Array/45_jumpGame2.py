class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        """
        Optimize:

        Max Distance Travel

        """

        i = 0
        count = 0
        while (i < len(nums) - 1):
            if i + nums[i] >= len(nums) - 1:
                return count + 1
            
            end = i + nums[i] + 1
            
            curMax = i
            next_idx = i
            for j in range(i + 1, end):
                if j + nums[j] > curMax:
                    curMax = j + nums[j]
                    next_idx = j
            
            count += 1
            i = next_idx

        return count