# https://leetcode.com/problems/k-closest-points-to-origin/
from typing import List
class Solution:
    # uses python sorting, O(NlogN)
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # sort by x value
        points = sorted(points, key=lambda x: x[0]**2+x[1]**2, reverse=False)
        return points[:K]

# interesting use of kd-tree for fast kNN search when N is very large but K is small, O(KlogN)
# https://leetcode.com/problems/k-closest-points-to-origin/discuss/576025/Python-3-lines-kNN-search-using-kd-tree-(for-large-number-of-queries)
# https://en.wikipedia.org/wiki/K-d_tree
# idea is to use axis-aligned hyperplanes, each node = 1 axis/dimension (out of k dimensions, in this case k = 2)
# searching is O(logN), kinda like binary tree but extended to k dimensions
# track current best point, then go up one level, compare other side of hyperplane, if dist is less than curr best,
# we MAY find a better point there, so we must search, otherwise, go up 1 more level of recursion, and repeat
from scipy import spatial
class Solution_kdtree:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        tree = spatial.KDTree(points)
		# x is the origin, k is the number of closest neighbors, p=2 refers to choosing l2 norm (euclidean distance)
        distance, idx = tree.query(x=[0,0], k=K, p=2) 
        return [points[i] for i in idx] if K > 1 else [points[idx]]


# possible to do faster than O(NlogN), i.e. O(N) on average
# by using divide & conquer, quickselect (quick sort is still O(NlogN))
# on avg we half the array since we dont need to sort the other half (for quick select)
# so, N + N/2 + N/4 + ... ~= 2N = O(N)
class Solution_quickselect:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:        
        dist = lambda i: points[i][0] ** 2 + points[i][1] ** 2
        
        def partition(array, l, r):
            pivot = array[r] # how to use median of 3?
            a = l
            for i in range(l, r):
                if dist(i) <= dist(r):
                    array[i], array[a] = array[a], array[i]
                    a += 1
            array[a], array[r] = array[r], array[a]
            return a            
            
        def sort(array, l, r, K):
            if l < r:
                pivot = partition(array, l, r)
                if pivot == K:
                    return
                elif pivot < K:
                    sort(array, pivot + 1, r, K)
                else:
                    sort(array, l, pivot - 1, K)
        
        sort(points, 0, len(points) - 1, K)
        return points[:K]

# minheap also can be used, but won't be as fast as quickselect I think
import heapq
class Solution_heap:
    # TC: O(N * logK) bcos inserting 1 item into heap is logK, and we need to insert N items
    # SC: O(K) since our heap is of size K
    # practically this is actly faster than quickselect soln, i guess bcos of recursive stack
    # https://leetcode.com/problems/k-closest-points-to-origin/discuss/294389/Easy-to-read-Python-min-heap-solution-(-beat-99-python-solutions-)
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for (x, y) in points:
            dist = -(x*x + y*y)
            if len(heap) == K:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))
        
        return [(x,y) for (dist,x, y) in heap]

# priority queue (queue w/ priority system, which in this case is the distance from origin)
# uses heap as underlying data structure?
import queue
class Solution_queue:
    # time: O(N + NlogK)
    # space: O(K)
    def kClosest(self, points, K):
        dist = [point[0]**2 + point[1]**2 for point in points]
        q = queue.PriorityQueue()
        
        for i in range(len(points)):
            q.put((-dist[i], points[i]))
            if q.qsize() > K:
                q.get() # remove farthest point from queue
        
		res = []
        while K > 0:
            point = q.get()[1]
            res.append(point)
            K -= 1
        return res