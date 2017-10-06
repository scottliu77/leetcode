'''

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.




'''

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        return self.search(nums, 0, right)
        
    
    def search(self, nums, left, right):
        while left < right:
            if nums[left] < nums[right]:
                return nums[left]
            mid = (left + right) / 2
            if nums[left] > nums[mid]:
                return self.search(nums, left, mid)
            else:
                return self.search(nums, mid + 1, right)
        return nums[left]