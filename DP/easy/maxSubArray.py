from typing import List
# https://leetcode.com/problems/maximum-subarray/submissions/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:       
        sums = [0 for _ in range(len(nums))]
        sums[0] = nums[0]
        
        curr_max = sums[0]
        for i in range(1, len(nums)):
            sums[i] = max(nums[i], sums[i-1]+nums[i])
            curr_max = max(curr_max, sums[i])
            
        return curr_max