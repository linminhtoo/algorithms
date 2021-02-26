from functools import lru_cache
from typing import Dict, List
from collections import defaultdict
# https://leetcode.com/problems/longest-string-chain/discuss/?currentPage=1&orderBy=most_votes&query=
class Solution:
    # very slow, even with lru_cache, beats only 6%, takes 2300 ms
    def longestStrChain(self, words: List[str]) -> int:
        length_map = defaultdict(list)
        max_len = float('-inf')
        for word in words:
            length_map[len(word)].append(word)
            max_len = max(max_len, len(word))
        
        self.res = 0
        @lru_cache(None)
        def helper(curr_word: str, chain: int):
            self.res = max(self.res, chain)
            
            W = len(curr_word)
            if W == 1:
                return
            elif W + chain <= self.res: # prune DFS
                return
            
            for word in length_map[W - 1]: # worst case O(N)
                for i in range(W): # O(K) = O(16)
                    next_word = curr_word[:i] + curr_word[i+1:]
                    if next_word == word:
                        helper(next_word, chain + 1)
                helper(word, 1) # start a new chain
                        
        for word in length_map[max_len]:
            helper(word, 1)
        return self.res