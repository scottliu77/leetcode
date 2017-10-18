'''

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?



'''

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        first_row = first_col = False
        for j in xrange(len(matrix[0])):
            if matrix[0][j] == 0:
                first_row = True
        for i in xrange(len(matrix)):
            if matrix[i][0] == 0:
                first_col = True
        for row in xrange(1, len(matrix)):
            for col in xrange(1, len(matrix[row])):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0
        
        for row in xrange(1, len(matrix)):
            if matrix[row][0] == 0:
                for col in xrange(1, len(matrix[row])):
                    matrix[row][col] = 0
        for col in xrange(1, len(matrix[0])):
            if matrix[0][col] == 0:
                for row in xrange(1, len(matrix)):
                    matrix[row][col] = 0
        
        if first_row:
            for j in xrange(len(matrix[0])):
                matrix[0][j] = 0
        if first_col:
            for i in xrange(len(matrix)):
                matrix[i][0] = 0