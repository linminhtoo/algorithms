# https://leetcode.com/problems/maximum-length-of-pair-chain/submissions/
# related to lengthOfLIS, largestDivisibleSubset
from typing import List
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # sorting is really important! otherwise we'll miss out some relevant children
        pairs.sort(key=lambda x: x[0])
        
        dp = [1 for _ in range(len(pairs))]
        res = 0
        for i in range(len(pairs)):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i], dp[j]+1)
            res = max(res, dp[i])
        return res