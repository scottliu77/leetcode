'''


Given a binary tree, you need to find the length of Longest Consecutive Path in Binary Tree.

Especially, this path can be either increasing or decreasing. For example, [1,2,3,4] and [4,3,2,1] are both considered valid, but the path [1,2,4,3] is not valid. On the other hand, the path can be in the child-Parent-child order, where not necessarily be parent-child order.

Example 1:
Input:
        1
       / \
      2   3
Output: 2
Explanation: The longest consecutive path is [1, 2] or [2, 1].
Example 2:
Input:
        2
       / \
      1   3
Output: 3
Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].
Note: All the values of tree nodes are in the range of [-1e7, 1e7].

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
        def _helper(root):
            if not root:
                return 0, 0
            inc, dec = 1, 1
            if root.left:
                left_inc, left_dec = _helper(root.left)
                if root.val == root.left.val + 1:
                    dec = left_dec + 1
                if root.val == root.left.val - 1:
                    inc = left_inc + 1
            if root.right:
                right_inc, right_dec = _helper(root.right)
                if root.val == root.right.val + 1:
                    dec = max(dec, right_dec + 1)
                if root.val == root.right.val - 1:
                    inc = max(inc, right_inc + 1)
            self.ans = max(self.ans, dec + inc - 1)
            return inc, dec
        _helper(root)
        return self.ans