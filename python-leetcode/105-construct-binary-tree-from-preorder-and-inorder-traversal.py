'''

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        d = {}
        for index, val in enumerate(inorder):
            d[val] = index
        return self._helper(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1, d)
    
    def _helper(self, preorder, pre_left, pre_right, inorder, in_left, in_right, d):
        if pre_right < pre_left or in_right < in_left:
            return None
        curr = preorder[pre_left]
        index = d[curr]
        node = TreeNode(curr)
        node.left = self._helper(preorder, pre_left + 1, pre_left + index - in_left, inorder, in_left, index - 1, d)
        node.right = self._helper(preorder, pre_right + index - in_right + 1, pre_right, inorder, index + 1, in_right, d)
        return node