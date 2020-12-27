# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://leetcode.com/problems/average-of-levels-in-binary-tree/submissions/
# related to levelOrder/levelOrderBottom.py
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
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
            out.append(sum(this_level) / len(this_level))
        return out

from collections import defaultdict
class Solution_defaultdict:
    def averageOfLevels(self, root):
        if root is None:
            return []
        levels = defaultdict(list)
        queue = [(root, 1)]
        level = 0
        while queue:
            node, level = queue.pop(0)
            levels[level].append(node.val)
            if node.left is not None:
                queue.append((node.left, level + 1))
            if node.right is not None:
                queue.append((node.right, level + 1))
        return [sum(levels[i]) / len(levels[i]) for i in range(1, level + 1)]