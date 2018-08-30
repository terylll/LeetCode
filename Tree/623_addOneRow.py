# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if (root is None):
            return None
        if (d == 1):
            temp = TreeNode(v)
            temp.left = root
            return temp
            
        self.helper(root, v, d, 1)
        return root

    
    def helper(self, root, v, d, depth):
        if (root is None):
            return root
        if (depth == d - 1):
            left_node = TreeNode(v)
            right_node = TreeNode(v)
            left_node.left = root.left
            right_node.right = root.right
            root.left = left_node
            root.right = right_node
            return root
        
        root.left = self.helper(root.left, v, d, depth + 1)
        root.right = self.helper(root.right, v, d, depth + 1)
        return root