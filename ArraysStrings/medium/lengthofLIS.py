# https://leetcode.com/problems/longest-increasing-subsequence/discuss/667975/Python-3-Lines-dp-with-binary-search-explained
from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums):
        dp = []
        for elem in nums:
            ind = bisect_left(dp, elem)
            if ind == len(dp):
                dp.append(elem)
            else:
                dp[ind] = elem
        return len(dp)
    
class Solution:
    def lengthOfLIS(self, nums):
        dp = [10**10] * (len(nums) + 1)
        for elem in nums: dp[bisect_left(dp, elem)] = elem  
        return dp.index(10**10)