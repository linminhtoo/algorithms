from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.results = set()
        
        def helper(subarr_so_far):
            if len(subarr_so_far) == k:
                if frozenset(subarr_so_far) not in self.results and sum(subarr_so_far) == n:
                    self.results.add(frozenset(subarr_so_far))
            
            lower_bound = 1 if not subarr_so_far else subarr_so_far[-1]
            for i in range(lower_bound, 10):
                if i not in subarr_so_far:
                    helper(subarr_so_far + [i])
        
        helper([])
        return [list(x) for x in self.results]