'''

Given a set of distinct integers, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]



'''

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        
        # Given a number in binary like 1001, we select the elements at index 0 and 3
        
        nums.sort()
        # Iterating through 1 to 2^n
        for i in xrange(1 << len(nums)):
            temp = []
            for j in xrange(len(nums)):
                
                if i >> j & 1:
                    temp.append(nums[j])
            ans.append(temp)
        
        return ans