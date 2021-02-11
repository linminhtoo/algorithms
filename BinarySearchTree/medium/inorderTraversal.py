from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# NOTE: can take note of Morris algorithm I guess
# https://leetcode.com/problems/binary-tree-inorder-traversal/submissions/ (see Solution)
# it avoids recursive stack, and is O(1) in extra space as there is no need to maintain a stack as well (for iterative)
class Solution_iterative:
    # NOTE: not same as preorderTraversal
    # need to use while loop to exhaust left subtree
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        stack = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res

class Solution_recursive:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        res.extend(self.inorderTraversal(root.left))
        res.append(root.val)
        res.extend(self.inorderTraversal(root.right))
        return res

class Solution_recursive_helper:
    def helper(self, root, res):
        if not root:
            return []
        res.extend(self.helper(root.left, []))
        res.append(root.val)
        res.extend(self.helper(root.right, []))
        return res
        
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return self.helper(root, [])