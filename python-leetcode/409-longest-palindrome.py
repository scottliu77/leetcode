'''

Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

'''

from collections import defaultdict
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = defaultdict(int)
        for char in s:
            d[char] += 1
        odd = False
        odd_count = 0
        total = 0
        for key in d:
            if d[key] % 2 != 0:
                odd = True
                total += d[key] - 1
            else:
                total += d[key]
        return total + 1 if odd else total