# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        p1 = head
        p2 = head
        
        idx = 0
        while(idx < n):
            p2 = p2.next
            idx += 1
        
        if (p2 is None):
            return head
        
        while (p2.next is not None):
            p1 = p1.next
            p2 = p2.next
        
        p1.next = p1.next.next
        
        return head
        