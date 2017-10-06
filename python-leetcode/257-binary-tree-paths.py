'''
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]


'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        ans = []
        self._helper(root, "", ans)
        return ans
    
    def _helper(self, root, path, ans):
        if not root:
            return
        if not path:
            path = str(root.val)
        else:
            path = path + "->" + str(root.val)
        if root.left:
            self._helper(root.left, path, ans)
        if root.right:
            self._helper(root.right, path, ans)
        if not root.left and not root.right:
            ans.append(path)