from typing import List
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/39038/Kadane's-Algorithm-Since-no-one-has-mentioned-about-this-so-far-%3A)-(In-case-if-interviewer-twists-the-input)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp = float('+inf')
        res = 0
        for p in prices:
            minp = min(p, minp)
            res = max(res, p - minp)
        return res