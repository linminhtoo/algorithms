import operator
import bisect
from typing import List
# https://leetcode.com/problems/russian-doll-envelopes/submissions/
# https://leetcode.com/problems/russian-doll-envelopes/discuss/82796/A-Trick-to-solve-this-problem.
class Solution:
    def maxEnvelopes(self, en: List[List[int]]) -> int:
        en.sort(key=lambda x: (x[0], -x[1])) 
        # trick is to sort by w and then reverse h
        # this is bcos unlike below dp where we have luxury of checking both h[i] < h[j] & w[i] < w[j]
        # here, we wish to do binary search on just heights (patience sort)
        # if we have [4,6], [4,8], it is wrong for [4,8] to consider [4,6] since width doesnt fit
        # if we swap to [4,8], [4,6] then we ensure [4,6] cannot consider [4,8] since height of 8 > height of 6
        heights = [h for _, h in en] 
        res = []
        for h in heights:
            idx = bisect.bisect_left(res, h)
            res[idx:idx+1] = [h] # if idx > len(res), then res will expand by 1, otherwise, we just replace existing element
            # res.insert(idx, h) # cannot use insert as it will expand res by 1 every h, but this is wrong
        return len(res)
        

class Solution_TLE: # O(N^2) dp is not fast enough, TLE on 2nd last test case :((( 
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        envelopes.sort(key=operator.itemgetter(0,1)) # will sort by both width & height simultaneously
        # e.g. ensures [5,4] comes before [6,4], but also that [6,4] comes before [6,7] even if originally [6,7] was before [6,4]
        
        dp = [1 for _ in range(len(envelopes))]
        res = 1
        for i in range(len(envelopes)):
            for j in range(i):
                if envelopes[j][0] < envelopes[i][0] and envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i], dp[j]+1)
            res = max(res, dp[i])
        return res        