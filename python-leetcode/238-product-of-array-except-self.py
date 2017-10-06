'''
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)


'''

class Solution(object):
	'''
	O(n) time
	'''
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p = 1
        ans = []
        for i in xrange(len(nums)):
            ans.append(p)
            p *= nums[i]
        p = 1
        for i in xrange(len(nums) - 1, -1, -1):
            ans[i] *= p
            p *= nums[i]
        return ans