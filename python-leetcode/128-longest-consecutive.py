'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

'''

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        d = {}
        for num in nums:
            if num in d:
                continue
            left = right = 0
            if num - 1 in d:
                left = d[num - 1]
            if num + 1 in d:
                right = d[num + 1]
            total = left + right + 1
            d[num] = total
            d[num - left] = total
            d[num + right] = total
            res = max(res, total)
        return res