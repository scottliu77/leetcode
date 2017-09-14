'''

Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

'''


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = dict()
        for char in s:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
        for char in t:
            if char not in d:
                return False
            d[char] -= 1
        
        for val in d.values():
            if val != 0:
                return False
            
        return True