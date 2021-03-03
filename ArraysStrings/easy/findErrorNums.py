from typing import List
from collections import defaultdict
class Solution:
    # time O(N)
    # space O(1) (no extra space complexity)
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = [0, 0]
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] < 0:
                res[0] = abs(nums[i]) # duplicate number
            else:
                nums[abs(nums[i]) - 1] *= -1 # multiply by -1
        
        for i in range(len(nums)):
            if nums[i] > 0:
                res[1] = i+1 # missing number
                
        return res

class Solution_space2N:
    # time O(N)
    # space O(N) (total O(2N))
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # count which number appeared twice by finding in a dict
        seen = defaultdict(int)
        # we can also count which number did not appear in this dict
        res = [0, 0]
        for num in nums:
            if num in seen:
                res[0] = num # number that occured twice
            seen[num] += 1
            
        for num in range(1, n+1):
            if num not in seen:
                res[1] = num
                break
        
        return res
                