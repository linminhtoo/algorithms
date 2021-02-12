# https://leetcode.com/problems/path-sum/discuss/36486/Python-solutions-(DFS-recursively-DFS%2Bstack-BFS%2Bqueue)
# https://leetcode.com/problems/path-sum/submissions/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # this is recursive, DFS
    def isLeaf(self, node):
        if not node:
            return True
        return not node.left and not node.right
    
    def DFS(self, node, sumsofar, target):
        if not node:
            return False
        sumsofar += node.val
        if sumsofar == target and self.isLeaf(node):
            return True
    
        found = False
        if node.left:
            found = self.DFS(node.left, sumsofar, target)
        if node.right and not found:
            found = self.DFS(node.right, sumsofar, target)
            
        return found
        
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        return self.DFS(root, 0, targetSum)