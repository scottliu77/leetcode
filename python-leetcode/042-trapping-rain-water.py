'''

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 

Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

'''

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        total = 0
        left_max = right_max = 0
        while left <= right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if left_max < right_max:
                total += (left_max - height[left])
                left += 1
            else:
                total += (right_max - height[right])
                right -= 1
        
        return total
        