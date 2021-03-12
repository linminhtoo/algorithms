try:
    from math import comb # only in Python 3.8 & onwards
except:
    import math
    def comb(n, r):
        return math.factorial(n) // math.factorial(r) // math.factorial(n-r)

# https://leetcode.com/problems/number-of-good-pairs/
from typing import List
from collections import defaultdict
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashmap = defaultdict(list)
        for i, num in enumerate(nums):
            hashmap[num].append(i)
          
        # [1] --> 0
        # [1, 1] --> 2
        # [1, 1, 1] --> 3
        # [1, 1, 1, 1] --> 6
        # formula = nC2
        res = 0
        for _, value in hashmap.items():
            if len(value) > 1:
                N = len(value)
                res += comb(N, 2)
                
        return res
        