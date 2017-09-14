'''

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if not len(stack):
                    return False
                temp = stack.pop()
                if char == ')' and not temp == '(':
                    return False
                if char == '}' and not temp == '{':
                    return False
                if char == ']' and not temp == '[':
                    return False
                
        return True if not len(stack) else False