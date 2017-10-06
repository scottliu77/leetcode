'''

Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?


'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import math

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        n = 0
        tracker = head
        while tracker:
            tracker = tracker.next
            n += 1
        second = head
        for i in xrange(int(math.ceil(n/2.0))):
            second = second.next
        back = self.reverse(second)
        while back:
            if head.val != back.val:
                return False
            back = back.next
            head = head.next
        return True
    
    def reverse(self, head):
        before = None
        while head:
            curr = head
            head = head.next
            curr.next = before
            before = curr
        return before