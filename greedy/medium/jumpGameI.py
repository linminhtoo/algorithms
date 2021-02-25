# https://leetcode.com/problems/jump-game/submissions/
from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest_idx = 0
        for i in range(len(nums)):
            if furthest_idx < i:
                # check if position i could be reached based on current furthest_idx
                # if it cant be reached, we cant continue, so False
                return False
            furthest_idx = max(furthest_idx, nums[i] + i)
        return True