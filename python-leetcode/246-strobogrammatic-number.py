'''

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

For example, the numbers "69", "88", and "818" are all strobogrammatic.

'''

class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        for i in xrange(len(num)/2 + 1):
            if num[i] != '6' and num[i] != '9' and num[i] != '1' and num[i] != '8' and num[i] != '0':
                return False
            if num[i] == '6' and num[len(num) - 1 - i] != '9':
                return False
            if num[i] == '9' and num[len(num) - 1 - i] != '6':
                return False
            if num[i] == '1' and num[len(num) - 1 - i] != '1':
                return False
            if num[i] == '8' and num[len(num) - 1 - i] != '8':
                return False
            if num[i] == '0' and num[len(num) - 1 - i] != '0':
                return False
        return True