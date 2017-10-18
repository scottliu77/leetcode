'''

Given a sorted integer array where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].


'''

class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        res = []
        if not nums:
            left, right = lower, upper
            if left == right:
                res.append(str(left))
            elif left < right:
                res.append(str(left) + "->" + str(right))
        for i in xrange(len(nums)):
            left = right = 0
            if i == 0:
                left = lower
                right = nums[i] - 1
            else:
                left = nums[i-1] + 1
                right = nums[i] - 1
            if left == right:
                res.append(str(right))
            elif left < right:
                res.append(str(left) + "->" + str(right))
        if nums:
            left = nums[-1] + 1
            right = upper
            if left == right:
                res.append(str(right))
            elif left < right:
                res.append(str(left) + "->" + str(right))
        return res