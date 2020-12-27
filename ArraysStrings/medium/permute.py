import math 
from copy import deepcopy
from typing import List
# https://leetcode.com/problems/permutations/discuss/18296/Simple-Python-solution-(DFS).
# backtracking
class Solution:
    def nextPermutation(self, input):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums = deepcopy(input)
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
        
        return nums
            
            
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = [nums]
        count = 1
        while count < math.factorial(len(nums)):

            next_perm = self.nextPermutation(nums)
            out.append(next_perm)
            nums = next_perm

            count += 1
            
            
        return out