from collections import defaultdict
from string import ascii_lowercase
from typing import List
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        letters_dict = defaultdict(int)
        for l in letters:
            letters_dict[l] += 1
        l_to_n = {l:idx for idx, l in enumerate(ascii_lowercase)} # map 'a' to 0, 'b' to 1 etc.
        
        # self.maxsofar = float('-inf')
        def helper(idx, letters_dict):            
            # no, do not form this word specified by this idx
            letters_dict = letters_dict.copy() # need this to avoid changing letters_dict from previous level of recursion
            if idx + 1 <= len(words) - 1:
                no = helper(idx + 1, letters_dict)
            else:
                no = 0
                
            # yes, form the word specified by this idx
            word = words[idx]
            yes = 0
            for letter in word:
                if letter in letters_dict and letters_dict[letter] > 0:
                    letters_dict[letter] -= 1
                    if letters_dict[letter] == 0:
                        del letters_dict[letter]
                    yes += score[l_to_n[letter]]
                else: # cant form this word
                    yes = 0
                    break
            if idx + 1 <= len(words) - 1:
                yes = yes + helper(idx + 1, letters_dict)
            
            # print(yes, no, idx, letters_dict)
            # self.maxsofar = max(self.maxsofar, max(yes, no)) # it is possible to prune search by stopping recursion once sum(words[idx:]) + current_score < maxsofar
            return max(yes, no)
            
        return helper(0, letters_dict)

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        score = [sum(score[ord(c)-ord('a')] for c in w) for w in words]
        words = list(map(Counter, words))
        
        # print(score)
        postfix_sum = [0 for _ in range(len(words))]
        postfix_sum[-1] = score[-1]
        i = len(words) - 2
        while i >= 0: # go backwards
            postfix_sum[i] = score[i] + postfix_sum[i+1]
            i -= 1
        # print(postfix_sum)

        self.res = 0
        def dfs(i, cur, c):
            # can replace sum(score[i:]) w/ postfix_sum[i]
            if i <= len(score) - 1 and cur + postfix_sum[i] <= self.res: # pruning
                return
            self.res = max(self.res, cur)
            for j, w in enumerate(words[i:], i):
                # this is basically checking that every letter in word can be subtracted by c
                # if that is the case, w - c = {} (empty) hence (not w - c) == True
                if not w - c:
                    dfs(j+1, cur + score[j], c - w)
        dfs(0, 0, Counter(letters))
        return self.res 
    