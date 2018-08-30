# Definition for a binary tree node.
class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if (root is None):
            return []
        
        res = []
        self.helper(root, 0, res)
        print(res)
        return res
        
    def helper(self, root, level, res):
        if (root is None):
            return
        
        if (level >= len(res)):
            res.append([root.val])
        else:
            # insert
            if (level % 2 == 0):
                res[level].append(root.val)
            else:
                res[level] = [root.val] + res[level]
            
        self.helper(root.left, level + 1, res)
        self.helper(root.right, level + 1, res)

root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)

sol = Solution()
print(sol.zigzagLevelOrder(root))
            