'''

Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
For example:
Given BST [1,null,2,2],
   1
    \
     2
    /
   2
return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).



'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	'''
	Runs in O(n) time and O(1) space
	Not the cleanest solutions as global variables are introduced. 
	'''
    modes = []
    currCount = maxCount = modeCount = 0
    currVal = None
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.find_modes(root, True)
        self.modes = [0] * self.modeCount
        self.modeCount = 0
        self.currCount = 0
        self.find_modes(root, False)
        return self.modes
    
    def find_modes(self, root, first):
        if not root:
            return
        self.find_modes(root.left, first)
        if root.val != self.currVal:
            self.currVal = root.val
            self.currCount = 0
        self.currCount += 1
        if self.currCount > self.maxCount:
            self.maxCount = self.currCount
            self.modeCount = 1
            if not first:
                self.modes[self.modeCount - 1] = self.currVal
        elif self.currCount == self.maxCount:
            if not first:
                self.modes[self.modeCount - 1] = self.currVal
            self.modeCount += 1
        self.find_modes(root.right, first)