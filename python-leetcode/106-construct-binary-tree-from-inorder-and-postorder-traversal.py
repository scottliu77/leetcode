'''

Given inorder and postorder traversal of a tree, construct the binary tree.

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
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        d = {}
        for index, val in enumerate(inorder):
            d[val] = index
        
        return self._helper(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1, d)
    
    def _helper(self, inorder, in_left, in_right, postorder, post_left, post_right, d):
        if in_right < in_left or post_right < post_left:
            return None
        curr = postorder[post_right]
        index = d[curr]
        node = TreeNode(curr)
        node.left = self._helper(inorder, in_left, index - 1, postorder, post_left, post_left + index - in_left - 1, d)
        node.right = self._helper(inorder, index + 1, in_right, postorder, post_right - in_right + index, post_right - 1, d)
        return node