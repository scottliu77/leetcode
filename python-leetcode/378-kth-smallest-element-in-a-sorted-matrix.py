'''
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note: 
You may assume k is always valid, 1 ≤ k ≤ n2.

'''

import heapq

class Solution(object):
    '''
    O(klogk) time complexity - k pushes onto the heap
    O(k) space
    '''
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap = []
        visited = set((0,0))
        heapq.heappush(heap, (matrix[0][0], (0, 0)))
        i = 1
        while i < k:
            tup = heapq.heappop(heap)[1]
            right = (tup[0], tup[1] + 1)
            down = (tup[0] + 1, tup[1])
            if right[1] < len(matrix) and right not in visited:
                heapq.heappush(heap, (matrix[right[0]][right[1]], right))
                visited.add(right)
            if down[0] < len(matrix[0]) and down not in visited:
                heapq.heappush(heap, (matrix[down[0]][down[1]], down))
                visited.add(down)
            i += 1
            
        
        return heap[0][0]