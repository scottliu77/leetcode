'''

Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
Note:
The input string length won't exceed 1000.

'''

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        for i in xrange(len(s)):
            total += self.expandCenter(s, i, i)
            total += self.expandCenter(s, i, i+1)
        return total
    
    def expandCenter(self, s, left, right):
        count = 0
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            else:
                return count
        return count