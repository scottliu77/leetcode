'''
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:


'''


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perim = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j]:
                    perim += self.calculate_adjacent_water(grid, i, j)
        return perim
                    
    def calculate_adjacent_water(self, grid, i, j):
        total = 4
        if i-1 >= 0:
            total -= grid[i-1][j]
        if i+1 < len(grid):
            total -= grid[i+1][j]
        if j-1 >= 0:
            total -= grid[i][j-1]
        if j+1 < len(grid[0]):
            total -= grid[i][j+1]
        return total