'''

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

'''

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
        if not head:
            return None
        d = {}
        curr = head
        while curr:
            d[curr] = RandomListNode(curr.label)
            curr = curr.next
        curr = head
        while curr:
            d[curr].next = d[curr.next] if curr.next in d else None
            d[curr].random = d[curr.random] if curr.random in d else None
            curr = curr.next
        return d[head]