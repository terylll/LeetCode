# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return self.helper(root, p, q)
    
    def helper(self, node, p, q):
        if (node is None):
            return None
        
        if (node.val == p.val or node.val == q.val):
            return node
        
        left = self.helper(node.left, p, q)
        right = self.helper(node.right, p, q)

        if (left is not None and right is not None):
            return node
        
        if (left is not None):
            return left
        
        if (right is not None):
            return right