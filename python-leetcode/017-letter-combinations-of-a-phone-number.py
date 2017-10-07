'''


Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.


'''

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d = {2:["a", "b", "c"], 3: ["d", "e", "f"], 4: ["g", "h", 'i'], 5: ["j", "k", "l"], 6: ["m", "n", "o"], 7: ["p", "q", "r", "s"], 8: ["t", "u", "v"], 9: ["w", "x", "y", "z"]}
        if not digits:
            return []
        return self._helper(list(digits), [[""]], d)
        
    def _helper(self, digits, res, d):
        if not digits:
            return ["".join(s) for s in res]
        c = int(digits[0])
        new_res = []
        for lis in res:
            for char in d[c]:
                new_res.append(lis + [char])
        return self._helper(digits[1:], new_res, d)