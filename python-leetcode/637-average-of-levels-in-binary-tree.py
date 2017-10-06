'''

Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.


'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        queue = deque()
        queue.append((root, 1))
        ans = []
        counts = []
        total = 0
        level = 1
        count = 0
        while queue:
            curr, curr_level = queue.popleft()
            if level != curr_level:
                ans.append(float(total)/count)
                total, count = 0, 0
                level += 1
            total += curr.val
            count += 1
            if curr.left:
                queue.append((curr.left, curr_level + 1))
            if curr.right:
                queue.append((curr.right, curr_level + 1))
        if count != 0:
            ans.append(float(total)/count)
        return ans