'''

Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.

Example 2:
Input: 9973
Output: 9973
Explanation: No swap.

Note:
The given number is in the range [0, 10^8]


'''

class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = [int(i) for i in str(num)]
        dp = [0] * len(digits)
        curr_max_pos = len(digits) - 1
        for i in xrange(len(digits) - 1, -1, -1):
            if digits[i] > digits[curr_max_pos]:
                curr_max_pos = i
            dp[i] = curr_max_pos
        
        for i in xrange(len(digits)):
            if not digits[dp[i]] == digits[i]:
                digits[i], digits[dp[i]] = digits[dp[i]], digits[i]
                break
        
        ans = 0
        for num in digits:
            ans = ans*10 + num
        
        return ans