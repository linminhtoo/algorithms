from typing import List
# https://leetcode.com/problems/range-sum-query-immutable/submissions/
class NumArray_runsum: # dp
    def __init__(self, nums: List[int]):
        # self.nums = nums
        # we can precompute the sums
        # sums have to be contiguous
        
        # bruteforce idea:
        # choices: 0 to 1, 2, 3, ..., len(nums)-1, bruteforce will be O(N^2) but should be optimizable
        # [1, 2, 3, 4]
        # 0, 2 --> 1 + 2 + 3 = 6
        # 1, 3 --> 2 + 3 + 4 = 9
        # dp[i][j+1] = sum(nums[i:j+1]) # nope, this is O(N^2) no matter how we look at it
        
        # new idea: use pre-fix/cumulative sums
        # sum[i] = sum(nums[0:i])
        # sumRange(i, j) = sum[j+1] - sum[i]
        
        # runsum = 0
        self.sums = [0] * (len(nums)+1)
        for i in range(len(nums)):
            self.sums[i+1] = self.sums[i] + nums[i]
        # for i in range(len(nums)+1):
        #     self.sums[i] = runsum
        #     if i <= len(nums) - 1:
        #         runsum += nums[i]
        
    def sumRange(self, i: int, j: int) -> int:
        return self.sums[j+1] - self.sums[i]              
        
class NumArray_bruteforce:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, i: int, j: int) -> int:
        return sum(self.nums[i:j+1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)