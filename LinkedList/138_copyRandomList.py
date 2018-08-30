# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """

        node_map = {}

        p = head

        while(p is not None):
            temp = RandomListNode()
            temp.label = p.label
            node_map[p] = temp
            p = p.next
        
        p = head
        res = node_map[p]
        while(p is not None):
            res.next = node_map[p.next]
            res.random = node_map[p.random]

            p = p.next
            res = res.next
            
        return node_map[head]