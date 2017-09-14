'''

You have k lists of sorted integers in ascending order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c if b-a == d-c.

Example 1:
Input:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
Output: [20,24]
Explanation: 
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
Note:
The given list may contain duplicates, so ascending order means >= here.
1 <= k <= 3500
-105 <= value of elements <= 105.
For Java users, please note that the input type has been changed to List<List<Integer>>. And after you reset the code template, you'll see this point.

'''

from heapq import heappush, heappop

class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        
        h = []

        # Initialize heap with first element from each of the arrays
        
        for i in range(len(nums)):
            heapq.heappush(h, (nums[i][0], i, 0))

        
        left = h[0][0]
        right = max(row[0] for row in nums)
        temp_right = max(row[0] for row in nums)
        
        while h:
            number, i, j = heapq.heappop(h)
            if temp_right - number < right - left:
                left, right = number, temp_right
            if j + 1 == len(nums[i]):
                return left, right
            temp_right = max(temp_right, nums[i][j+1])
            heapq.heappush(h, (nums[i][j+1], i, j+1))
                
            
        
        