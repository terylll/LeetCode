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
        
        if (head is None):
            return None
        


        list_len = 0
        t = head
        while(t.next is not None):
            list_len += 1
            t = t.next
        
        steps = k % (list_len + 1)
        
        slow = head
        count = 0
        while (count < steps):
            slow = slow.next
            count += 1
        
        fast = slow
        
        while (fast.next is not None):
            fast = fast.next
        
        res = slow.next
        slow.next = None
        fast.next = head
        return res

sol = Solution()

head = ListNode(None)
val = [1, 2]
t = head
for i in val:
    t.next = ListNode(i)
    t = t.next

res = sol.rotateRight(head.next, 2)

while (res is not None):
    print res.val
    res = res.next