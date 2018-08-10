# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root, 0)

    
    def helper(self, node, depth):
        if (node is None):
            return depth
        
        return max(self.helper(self.left, depth + 1), self.helper(self.right, depth + 1))