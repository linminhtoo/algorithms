from functools import lru_cache
from typing import Dict, List
from collections import defaultdict
# https://leetcode.com/problems/longest-string-chain/discuss/?currentPage=1&orderBy=most_votes&query=
class Solution_recursive_memoize:
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

class Solution_dp_notefficient: # try dp solution using lengthOfLIS
    # slow, 2292 ms, beats 7%, O(N^2)
    # this is slightly inefficient bcos there is no need to start j from 0
    # we make a lot of redundant calls to check(i, j)
    # we should instead, for words[j], generate all possible predecessors (up to 16 for this qns)
    # and check if we visited any of them already & retrieve that longest word chain length(will need to change dp table to dp dict)
    def longestStrChain(self, words: List[str]) -> int:
        # dp[i] = length of word chain ending in & that includes words[i]
        dp = [1 for _ in range(len(words))]
        words.sort(key=lambda x: len(x)) # super important!
        def check(i, j):
            # checks whether words[j] is a predecesssor of words[i]
            if len(words[i]) != len(words[j]) + 1:
                return False
            
            for k in range(len(words[i])):
                if words[i][:k] + words[i][k+1:] == words[j]:
                    return True
            return False # no matter where we remove one letter from words[i], we cannot get words[j]
        
        res = 1
        for i in range(len(words)):
            for j in range(i):
                if check(i, j):
                    dp[i] = max(dp[i], dp[j] + 1)
            res = max(res, dp[i])
        return res

class Solution_dp_fastest:
    # https://leetcode.com/discuss/general-discussion/1068411/Guide-to-Dynamic-Programming-Pattern%3A-Longest-Increasing-Subsequence
    # https://leetcode.com/problems/longest-string-chain/discuss/294890/JavaC%2B%2BPython-DP-Solution
    # much, much faster (124 ms, beats 91%)
    # time complexity = O(NSS) for dp where S = max(len(words[i])), O(NlogN) for sorting
    # space complexity = O(N)
    def longestStrChain(self, words: List[str]) -> int:
        dp = defaultdict(int)
        words.sort(key=len)
        res = 1
        for word in words:
            dp[word] = 1 # this is necessary to indicate that we can start a chain from word
            
            for i in range(len(word)): # up to 16 loops
                pred = word[:i] + word[i+1:] 
                # this can also cost up to O(max_len) = O(16) bcos we need to copy over & make a new string

                if pred in dp:
                    dp[word] = max(dp[word], dp[pred] + 1)
            res = max(res, dp[word])
        return res