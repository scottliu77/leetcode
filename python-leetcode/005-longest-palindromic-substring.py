'''

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"

'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        center = 0
        left = right = 0
        while center < len(s):
            left1, right1 = self.expand(s, center, center)
            left2, right2 = self.expand(s, center, center + 1)
            len1, len2 = right1 - left1, right2 - left2
            if len1 > right - left:
                left, right = left1, right1
            if len2 > right - left:
                left, right = left2, right2
            center += 1
        return s[left: right + 1]
    
    def expand(self, s, left, right):
        L, R = left, right
        while L >= 0 and R < len(s):
            if s[L] == s[R]:
                L -= 1
                R += 1
            else:
                break
        return L + 1, R - 1