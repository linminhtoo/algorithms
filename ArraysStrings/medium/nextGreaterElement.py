# using next permutation idea
from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> List[int]:
        i = len(nums) - 1
        while i - 1 >= 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i == 0:
            return -1
        j = i - 1
        while j + 1 <= len(nums) - 1 and nums[j+1] > nums[i-1]:
            j += 1
        # print(i-1, j)
        nums[i-1], nums[j] = nums[j], nums[i-1]
        # print(nums)
        m = i
        n = len(nums) - 1
        while m < n:
            nums[m], nums[n] = nums[n], nums[m]
            m += 1
            n -= 1
        return int(''.join(list(map(str, nums))))
    def nextGreaterElement(self, n: int) -> int:
        nums = []
        while n:
            q, r = divmod(n, 10)
            nums.append(r)
            n = q
        nums = list(reversed(nums))
        # print('before next permutation', nums)
        out = self.nextPermutation(nums)      
        if out > 2**31 - 1:
            return -1        
        else:
            return out
        


class Solution_fastest:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(str(n))
        pivot = len(nums)-2
        while pivot>=0:
            if nums[pivot]<nums[pivot+1]:
                break
            pivot-=1
        if pivot<0:
            return -1
        for i in range(len(nums)-1,pivot,-1):
            if nums[i]>nums[pivot]:
                nums[i],nums[pivot]=nums[pivot],nums[i]
                break
        num = int(''.join(nums[:pivot+1]+nums[pivot+1:][::-1]))
        return num if num<2**31-1 else -1