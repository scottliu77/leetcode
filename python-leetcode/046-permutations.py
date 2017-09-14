'''

Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]



'''

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        self._helper(nums, [], ans)
        return ans
        
    def _helper(self, nums, curr, ans):
        if not nums:
            ans.append(curr)
        for i in xrange(len(nums)):
            self._helper(nums[:i] + nums[i+1:], curr + [nums[i]], ans)
            