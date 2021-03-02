from collections import Counter
from functools import lru_cache
from typing import List
# https://leetcode.com/problems/ones-and-zeroes/discuss/95808/0-1-knapsack-in-python
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        L = len(strs)
        strings = list(map(Counter, strs))        
        self.max_size = float('-inf')
        @lru_cache(None)
        def helper(curr_idx: int, m: int, n: int, subset_size: int):
            # prune the search when (L - 1) - curr_idx + 1 + subset_size <= self.max_size
            if L - curr_idx + subset_size <= self.max_size:
                return
            
            if curr_idx <= L - 1:
                if strings[curr_idx]['0'] <= m and strings[curr_idx]['1'] <= n:
                    # able to deduct strings[curr_idx] counter fully using current budget
                    self.max_size = max(self.max_size, subset_size + 1)
                    # take string at curr_idx
                    helper(curr_idx + 1, m - strings[curr_idx]['0'], n - strings[curr_idx]['1'], subset_size + 1)

                # don't take it
                self.max_size = max(self.max_size, subset_size)
                helper(curr_idx + 1, m, n, subset_size)
                
        # budget = Counter({'0':m,'1':n}) # cannot use Counter bcos it is unhashable (cannot memoize/lru_cache)
        helper(0, m, n, 0)
        return self.max_size