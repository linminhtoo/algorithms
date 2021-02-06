# https://leetcode.com/problems/delete-operation-for-two-strings/submissions/
# highly related to longestCommonSubsequence
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == "":
            return len(word2)
        elif word2 == "":
            return len(word1)
        
        dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        for i in range(len(word1) + 1):
            for j in range(len(word2) + 1):
                if i == 0 or j == 0:
                    continue
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(
                        dp[i-1][j],
                        dp[i][j-1]
                    )
        
        # find LCS first then minus it from sum of lengths
        return len(word1) + len(word2) - 2 * dp[len(word1)][len(word2)]