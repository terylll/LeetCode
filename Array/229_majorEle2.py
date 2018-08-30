class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        count1 = 0
        count2 = 0
        candidate1 = None
        candidate2 = None
        
        for i in range(len(nums)):
            if (nums[i] == candidate1):
                count1 += 1
            elif (nums[i] == candidate2):
                count2 += 1
            elif (count1 == 0):
                candidate1 = nums[i]
                count1 += 1
            elif (count2 == 0):
                candidate2 = nums[i]
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1

        return [i for i in [candidate1, candidate2] if nums.count(i) > len(nums) / 3]