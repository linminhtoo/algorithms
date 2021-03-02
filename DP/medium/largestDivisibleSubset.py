# https://leetcode.com/problems/largest-divisible-subset/submissions/
# linked to lengthOfLIS
from typing import List
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # dp[i] = max length of subset that includes nums[i]
        dp = [1 for _ in range(len(nums))]
        
        # as qns asks for optimal path, we need another array to store the linkages
        # this is similar to UFDS where root[i] = j means we go from i to j
        parent = [i for i in range(len(nums))]
        
        nums.sort() # so that all divisors of nums[i] appear before index i
        max_len = 1 # max length of subset so far
        max_pos = 0 # position to start the process of recovering the optimal path
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    # normally we just do dp[i] = max(dp[i], 1 + dp[j])
                    # but here, if dp[i] is indeed updated to 1 + dp[j], then
                    # we also need to update parent[i] to j
                    # ie links position i to position j
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        parent[i] = j
            if dp[i] > max_len:
                max_len = dp[i]
                max_pos = i
                
        # recover path
        res = []
        j = max_pos
        while parent[j] != j:
            res.append(nums[j])
            j = parent[j]
        res.append(nums[j])
        return res
                    
        