# https://leetcode.com/problems/palindrome-partitioning-ii/submissions/
# yes, can memoize both cut() & isPal()
class Solution:
    def minCut(self, s: str) -> int:
        pal_memo = [[None for _ in range(len(s))] for _ in range(len(s))]
        cut_memo = [[None for _ in range(len(s))] for _ in range(len(s))]
        def isPal(start, end, memo):
            if start >= end:
                return True

            if memo[start][end] != None:
                return memo[start][end]
            else:
                res = (s[start] == s[end]) and isPal(start+1, end-1, memo)
                memo[start][end] = res
                return res
        
        def cut(start, end, memo):
            if start == end or isPal(start, end, pal_memo):
                return 0
            
            if memo[start][end] != None:
                return memo[start][end]
            else:
                res = len(s)-1
                for i in range(start, end):
                    if isPal(start, i, pal_memo):
                        res = min(res, 1 + cut(i+1, end, memo))
                memo[start][end] = res
                return res
        
        return cut(0, len(s)-1, cut_memo)