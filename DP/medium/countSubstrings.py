# highly related to DP solution to longestPalindrome (substring)
# https://leetcode.com/problems/palindromic-substrings/submissions/
class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        
        count = 0
        for start in range(len(s)):
            dp[start][start] = True
            count += 1
        
        for start in range(len(s) - 1, -1, -1):
            # need to traverse backwards bcos dp[start+1][end-1] must already have been evaluated
            # need to expand 'end', it is just logical
            for end in range(start + 1, len(s)):
                if s[start] == s[end]:
                    if end - start == 1 or dp[start+1][end-1]:
                        dp[start][end] = True
                        count += 1
        
        return count