from typing import List
# https://leetcode.com/problems/next-permutation/
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        found = False
        for i in range(len(nums)-1, 0, -1): 
            if nums[i-1] < nums[i]:
                found = True
                break
        
        if not found:
            start = 0
        else:
            # to_swap = nums[i-1]
            candidate = float('+inf')
            for j in range(i, len(nums), 1):
                if nums[j] > nums[i-1]:
                    if nums[j] <= candidate: # need to track index j
                        candidate = nums[j]
                        index = j
                    # candidate = min(nums[j], candidate) # cannot use, as it loses index j
            nums[i-1], nums[index] = nums[index], nums[i-1]
            
            start = i
        
        # time to reverse
        end = len(nums) - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

class Solution_lessmemory_butabitslower:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #>right
        i = len(nums)-1
        while i-1>=0 and nums[i-1]>=nums[i]:
            i -=1
        #>left
        if i-1>=0:
            j = i
            while j<len(nums) and nums[j]>nums[i-1]:
                j +=1
            #swap the min-max number
            nums[i-1],nums[j-1] = nums[j-1],nums[i-1]
        m = i
        n = len(nums)-1
        while m < n:
            nums[m],nums[n] = nums[n],nums[m]
            m +=1
            n -=1