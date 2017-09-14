'''

You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:

Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.

Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.

'''


class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        nums_sum = 0
        for num in nums:
            nums_sum += num
        
        if nums_sum < S or not ((nums_sum + S) % 2 == 0):
            return 0
        
        S = (S + nums_sum) / 2
        dp = [0] * (S + 1)
        dp[0] = 1
        for num in nums:
            for i in range(S, num - 1, -1):
                dp[i] += dp[i - num]
        return dp[S]
            