# https://leetcode.com/problems/count-vowels-permutation/
from collections import defaultdict
class Solution:
    def countVowelPermutation(self, N: int) -> int:
        # dp[n]['a'] == number of strings of length n ending with 'a'
        dp = [defaultdict(int) for _ in range(N+1)]
        for c in 'aeiou':
            dp[1][c] = 1
        for n in range(2, N+1):
            dp[n]['a'] = dp[n-1]['e'] + dp[n-1]['u'] + dp[n-1]['i']
            dp[n]['e'] = dp[n-1]['a'] + dp[n-1]['i']
            dp[n]['i'] = dp[n-1]['e'] + dp[n-1]['o']
            dp[n]['o'] = dp[n-1]['i']
            dp[n]['u'] = dp[n-1]['o'] + dp[n-1]['i']
        return (dp[N]['a'] + dp[N]['e'] + dp[N]['i'] + dp[N]['o'] + dp[N]['u']) % (10**9 + 7)
            