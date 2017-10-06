'''

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = [[]]
        if not root:
            return []
        self.dfs(root, 0, ans)
        return ans
        
    def dfs(self, root, level, ans):
        if level < len(ans):
            ans[level].append(root.val)
        else:
            ans.append([root.val])
        if root.left:
            self.dfs(root.left, level + 1, ans)
        if root.right:
            self.dfs(root.right, level + 1, ans)