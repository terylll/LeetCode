# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if (len(nums) == 0):
            return None
        
        return self.helper(nums, 0, len(nums) - 1)
    
    def helper(self, nums, start, end):
        """
        Convert nums[start ... end] to BST

        Base Case:
        start == end
            return TreeNode(nums[start])
        
        start + 1 == end
            

        """
        
        if (start == end or end == -1):
            return TreeNode(nums[start])

        if (start + 1 == end):
            node = TreeNode(nums[end])
            node.left = TreeNode(nums[start])
            return node
        
        mid = (start + end) / 2
        left = self.helper(nums, start, mid - 1)
        right = self.helper(nums, mid + 1, end)
        
        node = TreeNode(nums[mid])
        node.left = left
        node.right = right

        return node