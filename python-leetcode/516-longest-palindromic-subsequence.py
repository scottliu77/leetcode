'''

Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".


'''

class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [[-1 for j in xrange(len(s))] for i in xrange(len(s))]
        return self._helper(s, 0, len(s) - 1, dp)
    
    
    def _helper(self, s, start, end, dp):
        if dp[start][end] != -1:
            return dp[start][end]
        if start > end:
            return 0
        elif start == end:
            return 1
        elif s[start] == s[end]:
            dp[start][end] = 2 + self._helper(s, start + 1, end - 1, dp)
        else:
            dp[start][end] = max(self._helper(s, start + 1, end, dp), self._helper(s, start, end -1, dp))
        return dp[start][end]