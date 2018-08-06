# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        """
        Note the use of dummy node
        """
        
        if (head is None or head.next is None):
            return head
        
        dummy = ListNode(0)
        dummy.next = head

        fast = head
        slow = head

        length = 0
        while(fast.next != None):
            fast = fast.next
            length += 1
        
        i = 0
        while (i < length - k % length):
            slow = slow.next
            i += 1
        
        fast.next = dummy.next
        dummy.next = slow.next
        slow.next = None

        return dummy.next

        



a = ListNode(1)
b = ListNode(2)

a.next = b

sol = Solution()
print(sol.rotateRight(a, 0))