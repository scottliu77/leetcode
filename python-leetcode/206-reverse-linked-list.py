'''

Reverse a singly linked list.

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    '''
    Iterative Solution:
    O(n) time
    O(1) space

    '''
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        before = None

        while head:
            curr = head
            head = head.next
            curr.next = before
            before = curr
        
        return before
    
    '''
    Recursive Solution:
    O(n) time
    O(n) space

    '''
    def reverseListRecursive(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self._reverseHelper(head, None)
    
    def _reverseHelper(self, node, prev):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return self._reverseHelper(n, node);