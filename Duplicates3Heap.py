import logging
from typing import List

class Solution:
    @staticmethod
    #  [1, 5, 9, 1, 1], 1, 1)
    def containsNearbyAlmostDuplicate(nums: List[int], k: int, t: int) -> bool:
        '''  use a moving window of k + 1 numbers to build a Min Heap using heapq & check whether 
        difference is within t 
        '''
        left, right = 0, k
        min_heap = []
        for num in nums[left:right+1]:
            heapq.heappush(min_heap, num)
