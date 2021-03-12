import heapq
from collections import defaultdict
from typing import List
# https://leetcode.com/problems/sliding-window-maximum/submissions/
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # naive solution: just call max(window) as we iterate window from index 0 to len(nums) - k
        # this will definitely TLE for large k & N since complexity is O(Nk), and both can be up to 10^5
        
        # how to optimize? need to avoid calling max(window) everytime
        
        # can we do a single, forward pass, that keeps track of the max value so far, i.e. solve in O(N) time?
        # maybe we can use a hashset to store everytime we encounter a new max
        # {0 : 1, 1 : 3, 4 : 5, 6 : 6, 7 : 7} --> NOPE, won't work if we have many small numbers in the middle
        
        # use maxheap? from index = 0 to k-1, build heap of size k, then for index >= k, call heappushpop()
        # wont work, since we need to only consider k numbers every window, not all numbers from 0 to i
        
        # final idea that should work:
        # use maxheap, everytime we shift the sliding window, push num into heap & valid_nums.
        # valid_nums is just the dict of numbers in our current sliding window
        # then, peek at the max value (heap[0])
        # if heap[0] == last num that we moved away from (i.e. no longer in our sliding window), pop it
        # if heap[0] not in valid_nums dict, also pop it
        # time complexity should be O(NlogK) where K = size of maxheap, which shouldn't TLE
        res = [] # the list of k max's
        heap = []
        valid_nums = defaultdict(int)
        for i in range(0, k):
            valid_nums[nums[i]] += 1
            heapq.heappush(heap, -nums[i]) # negative to invert minheap to maxheap
        res.append(-heap[0])
            
        for i in range(k, len(nums)): # O(N)
            last = nums[i-k]
            valid_nums[last] -= 1 # O(1)
            valid_nums[nums[i]] += 1 # O(1)
            
            heapq.heappush(heap, -nums[i]) # O(logK)
            if -heap[0] == last: # O(1)
                heapq.heappop(heap) # O(logK)
            while valid_nums[-heap[0]] == 0:
                heapq.heappop(heap)
            res.append(-heap[0]) # O(1)
        return res

# https://leetcode.com/problems/sliding-window-maximum/discuss/1103840/O(n)-Fast-and-Readable
from collections import deque
class Solution_queue: # O(N)
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        l = r = 0
        res = []
        while r <= len(nums) - 1:
            while q and nums[q[-1]] < nums[r]: # dont need to consider all these smaller values since nums[r] is the new max
                q.pop()
            q.append(r) # add indices only to keep it simple (save memory)
            
            if l > q[0]: # pop element which is now out of window
                q.popleft()
            
            if r + 1 >= k: # at the beginning, to get window of size k first
                res.append(nums[q[0]])
                l += 1
            r += 1
        return res