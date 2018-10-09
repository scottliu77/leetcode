'''

Given a string, determine if a permutation of the string could form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True.

'''

from collections import defaultdict
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = defaultdict(int)
        for char in s:
            d[char] += 1
        odd = 0
        for key in d:
            if d[key] % 2 != 0:
                odd += 1
        return odd <= 1