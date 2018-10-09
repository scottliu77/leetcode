'''

Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Return 4
The longest increasing path is [1, 2, 6, 9].

Example 2:

nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Return 4
The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.




'''



class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        dp = [[0 for j in xrange(len(matrix[0]))] for i in xrange(len(matrix))]
        visited = [[0 for j in xrange(len(matrix[0]))] for i in xrange(len(matrix))]
        res = 0
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                dp[i][j] = self._checkNeighbors(matrix, i, j, dp)
                res = max(res, dp[i][j])
        return res
                
        
    
    def _checkNeighbors(self, matrix, row, col, dp):
        max_len = 0
        if row + 1 < len(matrix) and matrix[row][col] < matrix[row + 1][col]:
            if dp[row + 1][col] == 0:
                dp[row + 1][col] = self._checkNeighbors(matrix, row + 1, col, dp)
            max_len = max(max_len, dp[row + 1][col])
        if row - 1 >= 0 and matrix[row][col] < matrix[row - 1][col]:
            if dp[row - 1][col] == 0:
                dp[row - 1][col] = self._checkNeighbors(matrix, row - 1, col, dp)
            max_len = max(max_len, dp[row - 1][col])
        if col + 1 < len(matrix[0]) and matrix[row][col] < matrix[row][col + 1]:
            if dp[row][col + 1] == 0:
                dp[row][col + 1] = self._checkNeighbors(matrix, row, col + 1, dp)
            max_len = max(max_len, dp[row][col + 1])
        if col - 1 >= 0 and matrix[row][col] < matrix[row][col - 1]:
            if dp[row][col - 1] == 0:
                dp[row][col - 1] = self._checkNeighbors(matrix, row, col - 1, dp)
            max_len = max(max_len, dp[row][col - 1])
        return max_len + 1