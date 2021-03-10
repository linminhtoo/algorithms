from typing import List
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        nums_backwards = nums.copy()[::-1]
        
        changed = 0 
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                changed += 1
                nums[i+1] = nums[i]
            if changed > 2:
                break
                
        changed_back = 0
        for i in range(len(nums) - 1):
            if nums_backwards[i] < nums_backwards[i+1]:
                changed_back += 1
                nums_backwards[i+1] = nums_backwards[i]
            if changed_back > 2:
                break
                
        return changed <= 1 or changed_back <= 1