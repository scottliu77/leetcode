'''
Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

For example,
   1
    \
     3
    / \
   2   4
        \
         5
Longest consecutive sequence path is 3-4-5, so return 3.
   2
    \
     3
    / 
   2    
  / 
 1
Longest consecutive sequence path is 2-3,not3-2-1, so return 2.

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        if not root:
            return self.ans
        def _helper(root, curr):
            if not root:
                self.ans = max(self.ans, curr)
                return
            if root.left and root.val + 1 == root.left.val:
                _helper(root.left, curr + 1)
            else:
                self.ans = max(self.ans, curr)
                _helper(root.left, 1)
            if root.right and root.val + 1 == root.right.val:
                _helper(root.right, curr + 1)
            else:
                self.ans = max(self.ans, curr)
                _helper(root.right, 1)
        _helper(root, 1)
        return self.ans
            
