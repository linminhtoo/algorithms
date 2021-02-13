# https://leetcode.com/problems/path-sum-iii/submissions/
# https://leetcode.com/problems/path-sum-iii/discuss/141424/Python-step-by-step-walk-through.-Easy-to-understand.-Two-solutions-comparison.-%3A-)
# nice explanation of bruteforce + memoization

# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import defaultdict
class Solution:
    # 52 ms
    # memoization, O(N) time complexity since we visit each node only once
    # but sacrifice some space complexity --> now need O(N) extra space
    def DFS(self, root, target, sumsofar, cache):
        if root:
            sumsofar += root.val
            self.res += cache[sumsofar - target]
            cache[sumsofar] += 1
            
            self.DFS(root.left, target, sumsofar, cache)
            self.DFS(root.right, target, sumsofar, cache)

            cache[sumsofar] -= 1
    
    def pathSum(self, root, target):
        cache = defaultdict(int) 
        cache[0] = 1 # oldPathSum --> 1 way to have sum of 0
        self.res = 0
        self.DFS(root, target, 0, cache)
        return self.res

class Solution_bruteforce:
    # accepted
    # bruteforce, O(N^2) (732 ms)
    # bcos O(N) to visit each node via DFS and then another O(N) to check for paths via DFS
    def check(self, root, target):
        if root:
            if target == 0:
                self.res += 1
            self.check(root.left, target - root.left.val)
            self.check(root.right, target -  root.right.val)
    
    def DFS(self, root, target):
        if root:
            self.check(root, target - root.val)
            self.DFS(root.left, target)
            self.DFS(root.right, target)
    
    def pathSum(self, root: TreeNode, target: int) -> int:
        self.res = 0
        self.DFS(root, target)
        return self.res
        