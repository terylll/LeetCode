# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if (self.dfs(root) != -1):
            return True
        else:
            return False

    
    def dfs(self, node):
        if (node is None):
            return 0
        
        left = self.dfs(node.left) + 1
        right = self.dfs(node.right) + 1

        if (abs(left - right) > 2 or left == -1 or right == -1):
            return -1
        else:
            return max(left, right)
        
        