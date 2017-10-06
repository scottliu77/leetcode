'''


Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].

'''

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        n = len(matrix[0]) if m > 0 else 0
        top, left, bottom, right = 0, 0, m, n
        ans = []
        step = 1
        while top < bottom and left < right:
            for i in xrange(left, right, step):
                ans.append(matrix[top][i])
            top += 1
            if top == bottom:
                break
            for i in xrange(top, bottom, step):
                ans.append(matrix[i][right - 1])
            right -= 1
            if left == right:
                break
            step = -1 * step
            for i in xrange(right - 1,left - 1, step):
                ans.append(matrix[bottom - 1][i])
            bottom -= 1
            if top == bottom:
                break
            for i in xrange(bottom - 1, top - 1, step):
                ans.append(matrix[i][left])
            left += 1
            if left == right:
                break
            step = -1 * step
        return ans