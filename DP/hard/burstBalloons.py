from typing import List
# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/570/week-2-december-8th-december-14th/3564/
# https://www.youtube.com/watch?v=8RIqJDDgtU8 Errichto stream
class Solution: # not sure why it takes 9000 ms, probably the part about the window sizes
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + [num for num in nums if num > 0] + [1]
        N = len(nums) - 2
        dp_len = N + 2
        dp = [[0] * dp_len for _ in range(dp_len)]
        for window in range(1, N+1): # window sizes
            for left in range(1, (N - window + 1) + 1):
                right = left + window - 1       
                for k in range(left, right + 1):
                    # print(f'window {window}, left {left}, right {right}, k {k}')
                    dp[left][right] = max(dp[left][right],
                         nums[left-1] * nums[k] * nums[right+1] + dp[left][k-1] + dp[k+1][right])
        return dp[1][N]