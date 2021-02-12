# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/submissions/
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    '''
    Time complexity is O(N) to visit each node, but we also have to reverse every other level
    I think this is = num levels * length of each level = O(logN) (base2) * O(2^N)
    but overall solutions is fast, beats 98%

    Space complexity is O(N) since we have to put every node into the q
    '''
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        lvl_idx = 0
        q = [root]
        while q:
            lvl_res = []
            lvl_cnt = len(q)
            while lvl_cnt:
                curr = q.pop(0) # popleft
                lvl_res.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                lvl_cnt -= 1
            if lvl_idx % 2 == 1:
                lvl_res = lvl_res[::-1]
            res.append(lvl_res)
            lvl_idx += 1
        return res