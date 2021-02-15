from collections import defaultdict, deque
from typing import List
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return 0
        
        L = len(beginWord)
        combos = defaultdict(list)
        for word in wordList:
            for i in range(L):
                combos[word[:i] + '*' + word[i+1:]].append(word)
                
        queue = deque([(beginWord, 1)])
        visited = set([beginWord])
        while queue:
            curr, dist = queue.popleft()
            if curr == endWord:
                return dist
            
            for i in range(L):
                curr_generic = curr[:i] + '*' + curr[i+1:]
                candidates = combos[curr_generic]
                for cand in candidates:
                    if cand not in visited:
                        queue.append((cand, dist + 1))
                        visited.add(cand)
        
        return 0
                  