'''
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]

'''

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = [["." for i in xrange(n)] for j in xrange(n)]
        res = []
        self._dfs(board, 0, res)
        return res
        
    def _dfs(self, board, row, res):
        if row == len(board):
            res.append(self._create_board(board))
            return
        for j in xrange(len(board)):
            if self.is_safe(board, row, j):
                board[row][j] = "Q"
                self._dfs(board, row + 1, res)
                board[row][j] = "."
    
    def is_safe(self, board, row, col):
        for i in xrange(row):
            if board[i][col] == "Q":
                return False    
        x, y = row, col
        while x >= 0 and y >= 0:
            if board[x][y] == "Q":
                return False
            x -= 1
            y -= 1
        x,y = row, col
        while x >= 0 and y < len(board):
            if board[x][y] == "Q":
                return False
            x -= 1
            y += 1
        return True
    
    def _create_board(self, board):
        res = []
        for i in xrange(len(board)):
            res.append("".join(board[i]))
        return res