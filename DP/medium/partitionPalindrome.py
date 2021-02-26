# https://leetcode.com/problems/palindrome-partitioning/
from typing import List
class Solution:
    # downside of this is it is difficult to memoize
    # will be too slow when len(S) is large, like >= 49 already TLE
    # this is a problem for partitionII
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s: str, path: List[str], res: List[List[str]]) -> None:
        if not s:
            res.append(path)
            return
        for i in range(1, len(s)+1):
            if self.isPal(s[:i]):
                self.dfs(s[i:], path+[s[:i]], res)
        
    def isPal(self, s: str) -> bool:
        return s == s[::-1]