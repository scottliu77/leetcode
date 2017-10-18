'''

Given a string, find the length of the longest substring T that contains at most k distinct characters.

For example, Given s = “eceba” and k = 2,

T is "ece" which its length is 3.

'''


class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        start = res = 0
        d = {}
        for i in xrange(len(s)):
            d[s[i]] = i
            if len(d) > k:
                start = min(d.values())
                del d[s[start]]
                start += 1
            res = max(res, i - start + 1)
        return res