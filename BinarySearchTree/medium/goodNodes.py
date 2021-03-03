# https://leetcode.com/problems/count-good-nodes-in-binary-tree/submissions/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0 # total good nodes
        def inorder(node, maxsofar):
            if node:
                new_max = max(maxsofar, node.val)
                inorder(node.left, new_max)
                if maxsofar <= node.val:
                    self.res += 1 # this node is good
                inorder(node.right, new_max)
        inorder(root, float('-inf')) # safest is to set float('-inf') bcos Each node's value is between [-10^4, 10^4]
        return self.res
        
                