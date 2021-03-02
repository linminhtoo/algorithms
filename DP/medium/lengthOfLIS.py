from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] = length of max subsequence that ends at position i (must include position i)
        # this restriction allows us to form links/edges btwn two numbers (a, b) only if a < b
        # otherwise, if at position i, we just keep track of max length up to i (but may not include it), and return dp[len(nums) - 1]
        # HOWEVER it becomes more complicated how to transition from one dp state i_t to another i_t+1
        # with dp[i], the longest chain is probably not ending at position i, since nums[i] could be a very small number
        # hence, we need to keep track of max_len observed so far for dp[i] from i = 0 to i = len(nums) - 1
        # this is O(N^2) due to double loop
        dp = [1 for _ in range(len(nums))]
        res = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
            res = max(res, dp[i])
        return res