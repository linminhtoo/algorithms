# https://leetcode.com/problems/find-all-duplicates-in-an-array/submissions/

from typing import List
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen = set()
        out = []
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                out.append(num)
        
        return out

print(Solution().findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))
# [2, 3]
# 90% faster, but memory only less than 12% of other Python3 submissions

# all num in nums are positive. to use only O(1) space, use array itself as hashmap 
# hashing function is simply abs(x) or abs(x)-1, and change value to negative once it has been seen. 
# class Solution(object):
#     def findDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         res = []
#         for x in nums:
#             if nums[abs(x)-1] < 0:
#                 res.append(abs(x))
#             else:
#                 nums[abs(x)-1] *= -1
#         return res