from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mini, maxi, res = 1, 1, float('-inf')
        for num in nums:
            a = mini * num
            b = maxi * num
            mini = min(a, b, num)
            maxi = max(a, b, num)
            res = max(res, maxi)
        return res