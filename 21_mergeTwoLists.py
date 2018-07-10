"""
Link: https://leetcode.com/problems/merge-two-sorted-lists/description/
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        head = ListNode(None)
        cur = head
        
        """
        NOTICE: !None && !None
        """
        while (l1 is not None and l2 is not None):
            if (l1.val < l2.val):
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        if l2 is not None:
            cur.next = l2
        elif l1 is not None:
            cur.next = l1
        
        return head.next

l1_head = ListNode(1)
l1_head.next = ListNode(2)
l1_head.next.next = ListNode(4)

l2_head = ListNode(1)
l2_head.next = ListNode(3)
l2_head.next = ListNode(4)

sol = Solution()
print sol.mergeTwoLists(l1_head, l2_head)
