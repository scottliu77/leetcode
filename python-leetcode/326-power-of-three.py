'''


Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?


'''


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        if n > 1 and n % 3 == 0:
            return self.isPowerOfThree(n/3)
        if n == 1:
            return True
        return False