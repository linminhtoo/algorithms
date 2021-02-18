import random
from typing import List
class Solution:
    # quick select
    # should we add insertion sort for short lists?
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(nums, l, r, pivot_idx):
            pivot = nums[pivot_idx]
            nums[r], nums[pivot_idx] = nums[pivot_idx], nums[r]
            
            a = l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[a] = nums[a], nums[i]
                    a += 1
            
            nums[a], nums[r] = nums[r], nums[a]
            return a
            
        def sort(nums, l, r, K):
            if l < r:
                pivot_idx = random.randint(l, r)
                pivot_idx = partition(nums, l, r, pivot_idx)
                
                # K = smallest Kth element --> we need to enter K = L-k
                if pivot_idx == K:
                    return
                
                if pivot_idx < K:
                    sort(nums, pivot_idx+1, r, K)
                else:
                    sort(nums, l, pivot_idx-1, K)
                    
        L = len(nums)
        sort(nums, 0, L-1, L-k)
        return nums[L-k]
    
    # [1, 2, 3, 4]
    # 1st largest element --> (4) (1-indexed)
    # 3rd smallest element (1, 2, 3, 4) (0-indexed)

class Solution_heap:
    def findKthLargest(self, nums, k):
        heap = nums[:k]
        heapify(heap)
        for n in nums[k:]:
            heappushpop(heap, n)
        return heap[0]
        # this is smallest element of heap of K elements, so its the Kth largest 
        # (numbers smaller than this smallest element would have been popped out during heappushpop)