from typing import List
class Solution_memoize_TLE: # memoize TLE on last few test cases :(
    def scheduleCourse(self, C: List[List[int]]) -> int:
        # sort by deadline
        # do we just greedily add courses? but not sure if this will yield the maximum numebr of courses
        # eg we could have (very_large_t, small_d) followed by a bunch of 
        # (small_t, large_d), (small_t, large_d) which we should take and sacrifice the first course
        
        # CRITICAL! need to always first consider course w/ smaller deadline
        C.sort(key=lambda x: x[1])
        def schedule(i, time, memo):
            if i >= len(C):
                return 0
            if (i, time) in memo:
                return memo[(i, time)]
            else:
                if C[i][0] + time <= C[i][1]:
                    take = 1 + schedule(i+1, time+C[i][0], memo)
                else:
                    take = 0
                no_take = schedule(i+1, time, memo)
                memo[(i, time)] = max(take, no_take)
                return memo[(i, time)]
        
        # memoize
        return schedule(0, 0, {}) # index, curr_time

import heapq
class Solution: # priority queue is O(NlogN)
    def scheduleCourse(self, C: List[List[int]]) -> int:
        heap = [] # we maintain a maxheap (invert from minheap)
        # for each c in C, if c[0] + time <= c[1], add it
        # otherwise, peek at heap[0], if heap[0] > c[0]
        # time += c[0] - heap[0]
        # heapq.heappushpop(heap, c[0])
        C.sort(key=lambda x:x[1])
        time = 0
        for c in C:
            if c[0] + time <= c[1]:
                time += c[0]
                heapq.heappush(heap, -c[0])
            elif heap and -heap[0] > c[0]:
                time += c[0] - (-heap[0]) # time should decrease
                heapq.heappushpop(heap, -c[0])
        return len(heap)