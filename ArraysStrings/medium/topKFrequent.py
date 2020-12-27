from collections import Counter
from typing import List
# https://leetcode.com/problems/top-k-frequent-elements/submissions/
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter()
        for num in nums:
            counter[num] += 1
        # can just do counter = Counter(nums), lmoa
        
        out = []
        for num, freq in counter.most_common(k):
            out.append(num)
            
        return out

class Solution_heap:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        # O(1) time 
        if k == len(nums):
            return nums
        
        # 1. build hash map : character and how often it appears
        # O(N) time
        count = Counter(nums)   
        # 2-3. build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time
        return heapq.nlargest(k, count.keys(), key=count.get) 

# bucket sort approach - no freq can be more than N --> tells us that len(bucket) <= N, O(N) time & space
def topKFrequent(self, nums, k):
    bucket = [[] for _ in range(len(nums) + 1)]
    Count = Counter(nums).items()  
    for num, freq in Count: bucket[freq].append(num) 
    flat_list = [item for sublist in bucket for item in sublist]
    return flat_list[::-1][:k]