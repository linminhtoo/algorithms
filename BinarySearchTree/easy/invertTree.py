# https://leetcode.com/problems/invert-binary-tree/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        def helper(node):
            if node:
                node.left, node.right = node.right, node.left
                helper(node.left)
                helper(node.right)
        
        helper(root)
        return root