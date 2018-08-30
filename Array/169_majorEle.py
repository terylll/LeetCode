class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count = 0
        candidate = None
        for i in range(nums):
            if (candidate is None or count == 0):
                candidate = nums[i]
                count += 1
            else:
                if (candidate != nums[i]):
                    count -= 1
                else:
                    count += 1
        
        return candidate
    