'''

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.


'''

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or s[0] == '0':
            return 0
        a = b = 1
        for i in xrange(1, len(s)):
            temp = a
            curr = 0
            if s[i] != '0' and (s[i-1] == '1' or s[i-1] == '2' and s[i] <= '6'):
                curr += a + b
            elif s[i] == '0' and (s[i-1] == '1' or s[i-1] == '2' and s[i] <= '6'):
                curr += b
            elif s[i] != '0' and not (s[i-1] == '1' or s[i-1] == '2' and s[i] <= '6'):
                curr += a
            else:
                return 0
            a, b = curr, temp
        return a