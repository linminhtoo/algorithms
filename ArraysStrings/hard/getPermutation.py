# related to nextPermutation (medium)
# https://leetcode.com/problems/permutation-sequence/submissions/
from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 1
        while i - 1 >= 0 and nums[i-1] >= nums[i]:
            i -= 1
            
        if i - 1 >= 0:
            j = i
            while j + 1 <= len(nums) - 1 and nums[j+1] > nums[i-1]:
                j += 1
            nums[i-1], nums[j] = nums[j], nums[i-1]
        
        m = i
        n = len(nums) - 1
        while m < n:
            nums[m], nums[n] = nums[n], nums[m]
            m += 1
            n -= 1
        
    def getPermutation(self, n: int, k: int) -> str:
        nums = list(range(1, n+1))
        
        for i in range(k-1):
            self.nextPermutation(nums)
         
        return "".join(map(str, nums))

import math
class Solution_faster:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        numbers = range(1, n+1)
        permutation = ''
        k -= 1
        while n > 0:
            n -= 1
            # get the index of current digit
            index, k = divmod(k, math.factorial(n))
            permutation += str(numbers[index])
            # remove handled number
            numbers.remove(numbers[index])

        return permutation

class Solution_faster_string:
    def getPermutation(self, n, k):
        ns = [str(i+1) for i in range(n)]
        s = ""
        k -= 1
        while ns:
            q, k = divmod(k, math.factorial(n-1))
            s += ns.pop(q)
            n -= 1
        return s