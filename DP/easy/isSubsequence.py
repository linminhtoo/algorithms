# https://leetcode.com/problems/is-subsequence/submissions/
class Solution:
    def isSubsequence(self, S: str, T: str) -> bool:
        S = '0' + S # for when S = ''
        T = '0' + T # for when T = ''
        
        i = 0
        for t in T:
            if t == S[i]:
                i += 1
                if i == len(S):
                    return True
        
        return False

class Solution_binarysearch:
    def isSubsequence_1(self, s, t):
        start = 0
        for i in range(len(s)):
            start = t.find(s[i],start)
            if start==-1:
                return False
            start += 1
        return True

    def isSubsequence_2(self, s, t):
        for c in s:
            i = t.find(c)
            if i == -1:
                return False
            else:
                t = t[i+1:]
        return True