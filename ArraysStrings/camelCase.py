class Solution():
    def camelMatch(self, qs, p):
        def u(s):
            return [c for c in s if c.isupper()]

        def issup(s, t):
            it = iter(t) # iter is quite hack
            return all(c in it for c in s)
        return [u(p) == u(q) and issup(p, q) for q in qs]

class more_explainable_Solution():
    def camelMatch(self, qs, p):
        def u(s):
            return [c for c in s if c.isupper()]

        def issup(s, t):
            for c in s:
                if c in t:
                    t = t[t.index(c)+1:]
                else:
                    return False
            return True
            
        return [u(p) == u(q) and issup(p, q) for q in qs]

class easy_Solution():
    def camelMatch(self, inp: List[str], pat: str) -> List[bool]:
        def pat_match(str, pat):
            j = 0
            for i in str:
                if j < len(pat) and i == pat[j]:
                    j += 1
                elif ord('Z') >= ord(i) >= ord('A'):
                    return False
            return  j == len(pat) 

        res = []
        for i in inp:
            res.append(pat_match(i, pat))
        return res

import collections
from Typing import List
# Trie, don't understand the helper function recursion properly
class TrieNode:
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            cur = cur.child[char]
        cur.is_word = True

class Trie_Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        
        def find(node, p_i, pattern, cur_word, table):
            if p_i >= len(pattern):
                if node.is_word:
                    key = "".join(cur_word)
                    table[key] = True
                for k in node.child:
                    if k.islower():
                        find(node.child[k], p_i, pattern, cur_word+[k], table)
            else:
                for k in node.child:
                    if k == pattern[p_i]:
                        find(node.child[k], p_i+1, pattern, cur_word+[k], table)
                    elif k.islower():
                        find(node.child[k], p_i, pattern, cur_word+[k], table)
        
        trie = Trie()
        for q in queries:
            trie.insert(q)
        
        table = collections.defaultdict(lambda: False)
        find(trie.root, 0, pattern, [], table)

        return [table[q] for q in queries]

# https://leetcode.com/problems/camelcase-matching/discuss/270029/JavaC%2B%2BPython-Check-Subsequence-and-Regax