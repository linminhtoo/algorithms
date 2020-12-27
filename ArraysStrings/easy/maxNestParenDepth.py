# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/submissions/
class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        track = 0
        for char in s:
            if char == '(':
                track += 1
            elif char == ')':
                track -= 1
            count = max(count, track)
        return count