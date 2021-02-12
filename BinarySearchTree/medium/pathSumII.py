# https://leetcode.com/problems/path-sum-ii/
# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # DFS with stack
    # adapted directly from DFS with stack from pathSumI.py
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        stack = [(root, targetSum - root.val, [root.val])]
        while stack:
            node, val, visited = stack.pop()
            if not node.left and not node.right and val == 0:
                res.append(visited)
            if node.right:
                stack.append((node.right, val - node.right.val, visited + [node.right.val]))
            if node.left:
                stack.append((node.left, val - node.left.val, visited + [node.left.val]))
        return res