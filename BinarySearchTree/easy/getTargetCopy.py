# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# https://leetcode.com/explore/featured/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3590/
# easy
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def dfs(node, target):
            if node is None:
                return None
            
            if node.val == target.val:
                return node
            
            left = dfs(node.left, target)
            if left is not None:
                return left
            
            right = dfs(node.right, target)
            if right is not None:
                return right
            
            return None
        
        return dfs(cloned, target)

# in the case of repeasted values in the tree, check origTree is target instead of origTree.val == target
class Solution_concise_DFS:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(origTree: TreeNode, clonedTree: TreeNode) -> TreeNode:
            if origTree:
                return origTree is target and clonedTree or \
                    dfs(origTree.left, clonedTree.left) or \
                    dfs(origTree.right, clonedTree.right)
        return dfs(original, cloned)