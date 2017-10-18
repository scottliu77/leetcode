'''
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.

'''

import random

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.quickselect(nums, 0, len(nums) - 1, len(nums) - k)
    
    def quickselect(self, nums, left, right, k):
        if left >= right:
            return nums[left]
        pivot = random.randint(left, right)
        mid = nums[pivot]
        nums[pivot], nums[right] = nums[right], nums[pivot]
        curr = left
        for i in xrange(left, right):
            if nums[i] <= mid:
                nums[i], nums[curr] = nums[curr], nums[i]
                curr += 1
        nums[right], nums[curr] = nums[curr], nums[right]
        if curr < k:
            return self.quickselect(nums, curr + 1, right, k)
        elif curr > k:
            return self.quickselect(nums, left, curr - 1, k)
        return nums[curr]