'''

Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7, 
A solution set is: 
[
  [7],
  [2, 2, 3]
]

'''

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        candidates.sort()
        self._backtrack(candidates, 0, target, [], ans)
        return ans
    
    def _backtrack(self, candidates, index, target, path, ans):
        if target == 0:
            ans.append(list(path))
            return
        elif target < 0:
            return
        for i in xrange(index, len(candidates)):
            path.append(candidates[i])
            self._backtrack(candidates, i, target - candidates[i], path, ans)
            path.pop()