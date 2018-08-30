class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution2(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        stack = []
        self.traverse(root, stack)
        
        prev_node = None
        cur_node = None
        while(stack):
            
            cur_node = stack.pop(-1)

            cur_node.right = prev_node
            prev_node = cur_node
        
        
    def traverse(self, root, stack):
        if (root is None):
            return

        stack.append(root)
        
        self.traverse(root.left, stack)

        self.traverse(root.right, stack)

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.helper(root)

    def helper(self, root):
        if (root is None):
            return None, None
        if (root.left is None and root.right is None):
            return root, root
        
        lstart, lend = self.helper(root.left)
        rstart, rend = self.helper(root.right)
        
        if (rstart is None):
            root.right = lstart
            root.left = None
        elif (lstart is not None):
            lend.right = rstart
            root.left = None
            root.right = lstart
        
        return root, rend
        

sol = Solution()
root = Node(1)
root.left = Node(2)
# root.right = Node(5)
root.left.left = Node(3)
# root.left.right = Node(4)
# root.right.right = Node(6)

sol.flatten(root)

while(root is not None):
    print(root.val)
    root = root.right
