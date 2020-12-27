from typing import List
# https://leetcode.com/problems/shuffle-the-array/submissions/
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        left = nums[:n]
        right = nums[n:]
        
        out = []
        for A, B in zip(left, right):
            out.append(A)
            out.append(B)
            
        return out