# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if (len(preorder) == 0 or len(inorder) == 0):
            return None
        
        return self.helper(preorder, inorder, 0, 0, len(inorder) - 1)
    

    def helper(self, preorder, inorder, prestart, instart, inend):
        if (prestart >= len(preorder) or instart > inend):
            return None
        
        root = TreeNode(preorder[prestart])
        root_idx = instart
        for i in range(instart, inend + 1):
            if (inorder[i] == root.val):
                root_idx = i
                break
        
        root.left = self.helper(preorder, inorder, root_idx + 1, instart, root_idx - 1)
        root.right = self.helper(preoder, inorder, prestart + root_idx - instart + 1, root_idx + 1, inend)

        return root
        