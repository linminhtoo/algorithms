# Segment Tree
# https://leetcode.com/articles/a-recursive-approach-to-segment-trees-range-sum-queries-lazy-propagation/

# BIT
# https://cs.stackexchange.com/questions/10538/bit-what-is-the-intuition-behind-a-binary-indexed-tree-and-how-was-it-thought-a
# https://leetcode.com/problems/range-sum-query-mutable/discuss/75753/Java-using-Binary-Indexed-Tree-with-clear-explanation

from typing import List
class NumArray_SegmentTree:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.tree = [0] * (len(nums) * 4)
        def buildSegTree(t, l, h):
            if l == h:
                self.tree[t] = nums[l]
                return
            else:
                m = l + (h - l) // 2
                buildSegTree(2*t+1, l, m) # left child
                buildSegTree(2*t+2, m+1, h) # right child
                
                self.tree[t] = self.tree[2*t+1] + self.tree[2*t+2]
        buildSegTree(0, 0, len(nums)-1)    
    
    def sumRange(self, left: int, right: int) -> int:
        def querySegTree(t, l, h, i, j):
            if l > j or h < i: # segment out of range of query
                return 0
            if i <= l and j >= h: # segment entirely within query
                return self.tree[t]
            m = l + (h - l) // 2
            if i > m: # query range entirely to the right of mid
                return querySegTree(2*t+2, m+1, h, i, j)
            elif j <= m: # query range entirely to the left of mid
                return querySegTree(2*t+1, l, m, i, j)
            else: # we need to split our query range & combine the results
                leftquery = querySegTree(2*t+1, l, m, i, m)
                rightquery = querySegTree(2*t+2, m+1, h, m+1, j)
                return leftquery + rightquery
        return querySegTree(0, 0, len(self.nums)-1, left, right)
        
    def update(self, index: int, val: int) -> None:
        def updateSegTree(t, l, h, i, v):
            if l == h:
                self.tree[t] = v
                return
            
            m = l + (h - l) // 2
            if i > m:
                updateSegTree(t*2+2, m+1, h, i, v)
            else:
                updateSegTree(t*2+1, l, m, i, v)
            self.tree[t] = self.tree[t*2+1] + self.tree[t*2+2]
        updateSegTree(0, 0, len(self.nums)-1, index, val)
                
class NumArray_TLE: # this TLE :( 
    def __init__(self, nums: List[int]):
        # sums[i] = sum(nums[0:i])
        # but when we update(i, val), each of sums[i+1:] need to be updated, this is O(N)
        # but I guess this is fine, O(N) is acceptable
        self.nums = nums
        self.sums = [0] * (len(nums)+1)
        for i in range(len(nums)):
            self.sums[i+1] = self.sums[i] + nums[i]

    def update(self, index: int, val: int) -> None: # each update is O(N), up to 3*10^4 updates ~= 10^8 which is TLE
        # we need to optimize each update to O(1)
        for j in range(index+1, len(self.sums)):
            self.sums[j] += val - self.nums[index]
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right+1] - self.sums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)