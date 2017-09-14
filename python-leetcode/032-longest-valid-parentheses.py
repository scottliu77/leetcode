'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
'''

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 0
        max_len = 0
        
        for char in s:
            if char == '(':
                left += 1
            else:
                right += 1
                if left == right:
                    max_len = max(max_len, left * 2)
                if right > left:
                    left = 0
                    right = 0
        
        left = 0
        right = 0
        for char in reversed(s):
            if char == ')':
                right += 1
            else:
                left += 1
                if left == right:
                    max_len = max(max_len, right * 2)
                if right < left:
                    left = 0
                    right = 0
            
        
        return max_len