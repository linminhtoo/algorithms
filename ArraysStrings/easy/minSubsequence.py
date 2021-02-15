# https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/
from typing import List
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        
        total = sum(nums)
        
        res, res_sum = [], 0
        idx = 0
        while idx <= len(nums) - 1 and res_sum <= total - res_sum:
            res_sum += nums[idx]
            res.append(nums[idx])
            idx += 1
        
        return res