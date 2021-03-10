from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        seen = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in seen:
                return number