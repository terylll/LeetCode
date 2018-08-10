# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if (root is None ):
            return None
        
        left = self.trimBST(root.left, L, R)

        if (node.val > R):
            return left

        right = self.trimBST(root.right, L, R)

        if (node.val < L):
            return right
        
        root.left = left
        root.right = right

        return root
        
