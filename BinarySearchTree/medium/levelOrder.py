# https://leetcode.com/problems/binary-tree-level-order-traversal/
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = [root]
        while q:
            lvl_count = len(q)
            lvl_res = []
            while lvl_count:
                curr = q.pop(0) # popleft
                lvl_res.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                lvl_count -= 1
            res.append(lvl_res)
        return res