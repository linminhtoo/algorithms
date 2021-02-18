# from functools import lru_cache # doesnt work w/ list argument as it is unhashable
class Solution_recursion:
    # DFS recursion but not fast, beats 5% only in time
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = list(filter(lambda x: x <= target, candidates))
        if not candidates:
            return []
        
        L = len(candidates)
        suffix_sum = [0 for _ in range(L)]
        suffix_sum[-1] = candidates[-1]
        for i in reversed(range(L-1)):        
            suffix_sum[i] = suffix_sum[i+1] + candidates[i]
        suffix_sum.append(0) # needed when last idx of cand needs to be included but to prevent index out of range

        self.res = []
        def helper(idx, path, sumsofar):
            if sumsofar == target:
                path.sort()
                if path not in self.res:
                    self.res.append(path)
                return    
            if idx >= L or sumsofar > target:
                return
            
            this_cand = candidates[idx]
            if idx+1 <= L and suffix_sum[idx+1] + sumsofar + this_cand >= target:
                helper(idx+1, path+[this_cand], sumsofar+this_cand)
            if idx+1 <= L and suffix_sum[idx+1] + sumsofar >= target: 
                helper(idx+1, path, sumsofar)

        helper(0, [], 0)
        return self.res