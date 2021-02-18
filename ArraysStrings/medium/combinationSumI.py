# https://leetcode.com/problems/combination-sum/submissions/
from collections import deque
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        q = deque([((), 0)]) # (Tuple, sum) need tuple as it is hashable, while list isnt
        seen = set()
        res = []
        while q:
            curr, total = q.popleft()
            # print(curr, total, seen)
            if total == target:
                res.append(list(curr))
                curr = ()
                total = 0

            for cand in candidates:
                new = curr + (cand,)
                if total + cand <= target and new not in seen:
                    seen.add(new)
                    q.append((new, total + cand))
        
        # dont like this but only way to de-duplicate tuples 
        # eg (2, 3, 2) == (2, 2, 3) but only after listifying & sorting that list
        res_ = []
        for r in res:
            r = list(r)
            r.sort()
            if r not in res_:
                res_.append(r)
        return res_

class Solution_DFS_recursive_trim:
    def combinationSum(self, candidates, target):
        ret = []
        self.dfs(candidates, target, [], ret)
        return ret
    
    def dfs(self, nums, target, path, ret):
        if target < 0:
            return 
        if target == 0:
            ret.append(path)
            return 
        for i in range(len(nums)):
            # interesting
            # instd of keeping nums, he trims nums[i:] with i
            # enforce inherent order of candidates in all paths
            # this prevents duplicates!!!
            self.dfs(nums[i:], target-nums[i], path+[nums[i]], ret)