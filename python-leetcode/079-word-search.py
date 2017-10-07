'''

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.


'''

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        visited = [[False for j in xrange(len(board[0]))] for i in xrange(len(board))]
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    if self._helper(board, word[1:], i, j, visited):
                        return True
                    visited[i][j] = False
        return False
                
    
    def _helper(self, board, word, i, j, visited):
        if not word:
            return True
        target = word[0]
        if i-1 >= 0 and board[i-1][j] == target and not visited[i-1][j]:
            visited[i-1][j] = True
            if self._helper(board, word[1:], i-1, j, visited):
                return True
            visited[i-1][j] = False
        if i+1 < len(board) and board[i+1][j] == target and not visited[i+1][j]:
            visited[i+1][j] = True
            if self._helper(board, word[1:], i+1, j, visited):
                return True
            visited[i+1][j] = False
        if j-1 >= 0 and board[i][j-1] == target and not visited[i][j-1]:
            visited[i][j-1] = True
            if self._helper(board, word[1:], i, j-1, visited):
                return True
            visited[i][j-1] = False
        if j+1 < len(board[0]) and board[i][j+1] == target and not visited[i][j+1]:
            visited[i][j+1] = True
            if self._helper(board, word[1:], i, j+1, visited):
                return True
            visited[i][j+1] = False
        return False