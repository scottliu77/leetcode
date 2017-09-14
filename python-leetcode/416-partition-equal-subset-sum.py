'''
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.



'''

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = 0
        for num in nums:
            s += num
        
        if len(nums) < 2 or not s % 2 == 0:
            return False
        
        target = s / 2
        nums.sort()
        
        dp = [[1] * (target + 1)]
        for i in range(len(nums)):
            dp.append([1] + [0] * target)
        
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if nums[i-1] > j:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]
        
        return bool(dp[len(nums)][target])