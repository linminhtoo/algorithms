# https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/930/
# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://leetcode.com/problems/binary-tree-postorder-traversal/discuss/45551/Preorder-Inorder-and-Postorder-Iteratively-Summarization
# see comment from ofLucas
# The reverse of pre-order is skillful though may not be general. 
# Here I attach my solution of postorderTrav without reversing pre-order.
# The key point is when you pop a node from stack, you ensure you have already explored its children.
class Solution_iterative:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        def isLeaf(node):
            if not node: # only when we finished and want to break while curr loop
                return True
            return not node.left and not node.right
            
        res = []
        stack = []
        curr = root
        while curr or stack:
            while not isLeaf(curr):
                stack.append(curr)
                curr = curr.left
            if curr:
                res.append(curr.val)
            while stack and curr == stack[-1].right:
                curr = stack.pop() # what we popped is the parent of curr (which we explored already)
                res.append(curr.val)
            if not stack:
                curr = None # want to break while curr loop
            else:
                curr = stack[-1].right
        return res
        

class Solution_recursive:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        res.extend(self.postorderTraversal(root.left))
        res.extend(self.postorderTraversal(root.right))
        res.append(root.val)
        return res

class Solution_recursive_helper:
    def helper(self, root, res):
        if not root:
            return []
        res = []
        res.extend(self.helper(root.left, []))
        res.extend(self.helper(root.right, []))
        res.append(root.val)
        return res
        
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        return self.helper(root, [])