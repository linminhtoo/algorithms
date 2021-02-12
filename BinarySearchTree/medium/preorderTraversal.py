# https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/928/
# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution_recursive:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        res = []
        res.append(root.val)
        res.extend(self.preorderTraversal(root.left))
        res.extend(self.preorderTraversal(root.right))

        return res
            
class Solution_recursive_helper:
    def helper(self, root, res):
        if not root:
            return []
        res.append(root.val)
        res.extend(self.helper(root.left, []))
        res.extend(self.helper(root.right, []))
        return res
        
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        return self.helper(root, [])
            
class Solution_iterative:
    # not generalizable to in/post order Traversal
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            # NOTE: add curr.right to stack first since the stack is FILO
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return res