'''
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:
[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.




'''

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j]:
                    grid[i][j] = 0
                    curr = self._checkNeighbors(grid, i, j, 1)
                    ans = max(ans, curr)
        return ans
    
    def _checkNeighbors(self, grid, i, j, size):
        updated = size
        if i+1 < len(grid) and grid[i+1][j]:
            grid[i+1][j] = 0
            updated += self._checkNeighbors(grid, i+1, j, 1)
        if i-1 >= 0 and grid[i-1][j]:
            grid[i-1][j] = 0
            updated += self._checkNeighbors(grid, i-1, j, 1)
        if j+1 < len(grid[0]) and grid[i][j+1]:
            grid[i][j+1] = 0
            updated += self._checkNeighbors(grid, i, j+1, 1)
        if j-1 >= 0 and grid[i][j-1]:
            grid[i][j-1] = 0
            updated += self._checkNeighbors(grid, i, j-1, 1)
        return updated