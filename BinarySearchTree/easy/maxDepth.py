# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# https://leetcode.com/submissions/detail/433749213/?from=explore&item_id=3551
class Solution_fast:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth + 1, right_depth + 1)

class Solution_fast_v2: # slightly slower but actually it's exactly the same in principle as Solution_fast
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), 
                       self.maxDepth(root.right))

class Solution_mine:
    def maxDepth(self, root: TreeNode) -> int:
        def dfs(node, level):
            if not node:
                return level - 1
            left = dfs(node.left, level + 1)
            right = dfs(node.right, level + 1)
            return max(left, right)
        return dfs(root, 1)