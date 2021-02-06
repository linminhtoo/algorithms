# https://leetcode.com/problems/longest-common-subsequence/submissions/
class Solution:
    def longestCommonSubsequence(self, A: str, B: str) -> int:
        dp = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
        
        for a in range(1, len(A) + 1):
            for b in range(1, len(B) + 1):
                if A[a-1] == B[b-1]:
                    dp[a][b] = 1 + dp[a-1][b-1]
                else: 
                    dp[a][b] = max(
                        dp[a-1][b],
                        dp[a][b-1]
                    )
                    
        return dp[len(A)][len(B)]