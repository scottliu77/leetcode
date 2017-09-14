'''

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

Credits:

Special thanks to @ts for adding this problem and creating all test cases.


'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class TreeNodeWithCount(object):
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None
            self.count = 1
            
class Solution(object):
    
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        count_root = self._buildTree(root)
        self._updateCounts(count_root)
        #return count_root.right.count
        return self._helper(count_root, k)
        
        
    def _helper(self, root, k):
        left_count = 0
        if root.left is not None:
            left_count = root.left.count
        if k == left_count + 1:
            return root.val
        if k < left_count + 1:
            return self._helper(root.left, k)
        else:
            return self._helper(root.right, k - left_count - 1)
        
    
    def _buildTree(self, root):
        if root is None:
            return None
        count_root = TreeNodeWithCount(root.val)
        count_root.left = self._buildTree(root.left)
        count_root.right = self._buildTree(root.right)
        return count_root

    
    def _updateCounts(self, root):
        if root is None:
            return 0
        root.count = self._updateCounts(root.left) + self._updateCounts(root.right) + 1
        return root.count