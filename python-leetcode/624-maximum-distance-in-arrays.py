'''

Given m arrays, and each array is sorted in ascending order. Now you can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a-b|. Your task is to find the maximum distance.

Example 1:
Input: 
[[1,2,3],
 [4,5],
 [1,2,3]]
Output: 4
Explanation: 
One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
Note:
Each given array will have at least 1 number. There will be at least two non-empty arrays.
The total number of the integers in all the m arrays will be in the range of [2, 10000].
The integers in the m arrays will be in the range of [-10000, 10000].

'''

class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        if not arrays:
            return 0
        max_dist = 0
        curr_min = arrays[0][0]
        curr_max = arrays[0][-1]
        for i in xrange(1, len(arrays)):
            max_dist = max(max_dist, curr_max - arrays[i][0], arrays[i][-1] - curr_min)
            curr_min = min(curr_min, arrays[i][0])
            curr_max = max(curr_max, arrays[i][-1])
        return max_dist