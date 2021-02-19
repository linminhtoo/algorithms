# https://leetcode.com/problems/valid-parentheses/submissions/
from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        q = deque()
        pairs = {'(':')', '{':'}', '[':']'}
        for c in s:
            if c in pairs:
                q.append(c)
            else:
                if len(q) == 0 or pairs[q[-1]] != c:
                    return False
                else:
                    q.pop()
        return len(q) == 0
                               