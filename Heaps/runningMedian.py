from typing import List
# https://www.hackerrank.com/challenges/find-the-running-median/forum

# use minHeap & maxHeap!! 
class Solution:
    def running_median(self, nums: List[int]) -> List[float]:
        sorted_list = []
        for idx, num in enumerate(nums):
            add_pos = self.binary_search(sorted_list, num, len(sorted_list)//2)
            sorted_list.insert(add_pos - 1, num)
            if idx % 2 == 0: # even
                print(sorted_list[idx//2])
            else: # odd
                mean = (sorted_list[idx//2] + sorted_list[idx//2+1]) /2 
                print(mean) 

    # wrong, not binary_search, should use insertion_sort !! 
    # anyway this is modified binary_search
    def binary_search(self, nums: List[int], new: int, counter: int) -> int:
        if not nums: # empty list
            return counter
        # returns idx to insert new element
        mid = len(nums) // 2
        if new > mid: 
            mid = self.binary_search(nums[mid:], new, counter + len(nums[mid:])//2)
        else:
            mid = self.binary_search(nums[:mid], new, counter - len(nums[:mid])//2)

        return counter 
