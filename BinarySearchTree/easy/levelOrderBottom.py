#Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/submissions/
# v similar to levelOrder.py, just add 'reversed' at the end
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return
        
        out = []
        q = [root]
        while q:
            level = len(q)
            this_level = []
            while level:
                cur_node = q.pop(0)
                level -= 1
                this_level.append(cur_node.val)
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)
            out.append(this_level)
        
        return reversed(out)
                
# alternative, using deque (popleft & append (which is appendright))
class Solution_deque:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None: return
        queue = deque([root])
        output = []
        while queue:
            level = []
            for i in range(len(queue)): # similar idea as level -= 1, to capture the current level
                node = queue.popleft()
                level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            output.append(level)
        return output[::-1]