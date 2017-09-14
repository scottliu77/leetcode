'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:

Bonus points if you could solve it both recursively and iteratively.


'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return root is None or self._helper(root.left, root.right)
    
    def _helper(self, left, right):
        if left is None or right is None:
            return left == right
        if not left.val == right.val:
            return False
        return self._helper(left.right, right.left) and self._helper(left.left, right.right)