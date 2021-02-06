# https://leetcode.com/problems/partition-equal-subset-sum/submissions/

from typing import List
# https://leetcode.com/problems/partition-equal-subset-sum/discuss/90592/01-knapsack-detailed-explanation
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        else:
            target = total // 2
            
        dp = [[None for _ in range(target + 1)] for _ in range(len(nums) + 1)] # fill w/ dummy 0th row & col
        nums = [0] + nums
        
        def partition(idx: int, amt_left: int):
            if amt_left < 0: # must do here otherwise index out of range
                return False
            
            if dp[idx][amt_left] is None:
                if amt_left == 0:
                    result = True
                elif idx == 0:
                    result = False
                else:
                    if nums[idx] > amt_left:
                        result = partition(idx - 1, amt_left)
                    else:
                        A = partition(idx - 1, amt_left)
                        B = partition(idx - 1, amt_left - nums[idx])
                        result = A or B
                dp[idx][amt_left] = result
            else:
                result = dp[idx][amt_left]
            return result
        
        return partition(len(nums) - 1, target)