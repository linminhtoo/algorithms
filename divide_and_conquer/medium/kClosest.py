# https://leetcode.com/problems/k-closest-points-to-origin/
from typing import List
class Solution:
    # uses python sorting, O(NlogN)
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # sort by x value
        points = sorted(points, key=lambda x: x[0]**2+x[1]**2, reverse=False)
        return points[:K]

# possible to do faster than O(NlogN) on average
# by using divide & conquer, quickselect


# minheap also can be used, but won't be as fast as quickselect I think
        