# https://leetcode.com/problems/convert-bst-to-greater-tree/submissions/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.sum = 0
        def inverted_inorder(node):
            # node.right --> node --> node.left
            if node:
                inverted_inorder(node.right)
                self.sum += node.val
                node.val = self.sum
                inverted_inorder(node.left)
        
        inverted_inorder(root)
        return root