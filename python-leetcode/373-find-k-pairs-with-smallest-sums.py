'''
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first array and one element from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:

Given nums1 = [1,7,11], nums2 = [2,4,6],  k = 3

Return: [1,2],[1,4],[1,6]

The first 3 pairs are returned from the sequence:
[1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

Example 2:

Given nums1 = [1,1,2], nums2 = [1,2,3],  k = 2

Return: [1,1],[1,1]

The first 2 pairs are returned from the sequence:
[1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

Example 3:

Given nums1 = [1,2], nums2 = [3],  k = 3 

Return: [1,3],[2,3]

All possible pairs are returned from the sequence:
[1,3],[2,3]

'''

import Queue as queue

class Solution(object):

    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        
        class Pair(object):
            def __init__(self, priority, pair, nums1_index, nums2_index):
                self.priority = priority
                self.pair = pair
                self.nums1_index = nums1_index
                self.nums2_index = nums2_index
                

            def __cmp__(self, other):
                return cmp(self.priority, other.priority)

        ans = []
        heap = queue.PriorityQueue()
        
        if nums1 == None or nums2 == None or len(nums1) == 0 or len(nums2) == 0:
            return ans
        
        for i in range(len(nums1)):
            if i >= k:
                break
            heap.put(Pair(nums1[i] + nums2[0], [nums1[i], nums2[0]], i, 0))
        
        while k > 0 and not heap.empty():
            k -= 1
            curr = heap.get()
            ans.append(curr.pair)
            x = curr.nums1_index
            y = curr.nums2_index
            if y == len(nums2) - 1:
                continue
            heap.put(Pair(nums1[x] + nums2[y + 1], [nums1[x], nums2[y + 1]], x, y + 1))
        
        return ans
