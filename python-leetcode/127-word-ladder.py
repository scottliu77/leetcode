'''

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
UPDATE (2017/1/20):
The wordList parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.


'''


from collections import deque
from string import ascii_lowercase

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        unvisited = set(wordList)
        queue = deque()
        queue.append((beginWord, 1))
        while queue:
            word, length = queue.popleft()
            curr_word = list(word)
            for i in xrange(len(curr_word)):
                curr_letter = curr_word[i]
                for c in ascii_lowercase:
                    curr_word[i] = c
                    temp = ''.join(curr_word)
                    if temp in unvisited:
                        if temp == endWord:
                            return length + 1
                        queue.append((temp, length + 1))
                        unvisited.remove(temp)
                curr_word[i] = curr_letter
        return 0