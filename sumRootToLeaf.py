 # https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root, val=0):
        if not root: return 0
        val = val * 2 + root.val # convert binary to base 10
        if root.left == root.right: return val
        return self.sumRootToLeaf(root.left, val) + self.sumRootToLeaf(root.right, val)