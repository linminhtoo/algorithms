# https://leetcode.com/problems/degree-of-an-array/submissions/
from typing import List
from collections import defaultdict
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        degree = 0
        for num in nums:
            hashmap[num] += 1
            degree = max(degree, hashmap[num])
        
        candidates = []
        for k, v in hashmap.items():
            if v == degree:
                candidates.append(k)
                
        # print(candidates)
        min_length = float('+inf')
        for cand in candidates:
            for i in range(len(nums)):
                if nums[i] == cand:
                    break
            
            for k in reversed(range(len(nums))):
                if nums[k] == cand:
                    min_length = min(min_length, k - i + 1)
                    break
            
            # print(cand, i, k)
        return min_length

class Solution_onepass: # but essentially the same idea
    def findShortestSubArray(self, A):
        first, count, res, degree = {}, {}, 0, 0
        for i, a in enumerate(A):
            first.setdefault(a, i)
            count[a] = count.get(a, 0) + 1
            if count[a] > degree:
                degree = count[a]
                res = i - first[a] + 1
            elif count[a] == degree:
                res = min(res, i - first[a] + 1)
        return res