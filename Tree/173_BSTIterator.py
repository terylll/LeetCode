# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.iterator = []
        self.populate(root)
        self.curIdx = 0
    
    def populate(self, node):
        if (node is None):
            return None
        
        self.populate(node.left)
        self.iterator.append(node.val)
        self.populate(node.right)
        
        return 
        


    def hasNext(self):
        """
        :rtype: bool
        """
        return self.curIdx < len(self.iterator)
        

    def next(self):
        """
        :rtype: int
        """
        self.curIdx += 1
        return self.iterator(self.curIdx - 1)

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())