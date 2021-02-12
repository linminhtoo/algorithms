# Definition for a binary tree node.
# https://leetcode.com/problems/validate-binary-search-tree/submissions/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def helper(self, root, low, high):
        if not root:
            return True
        return (root.val > low and root.val < high) and \
            self.helper(root.left, low, root.val) and \
            self.helper(root.right, root.val, high)
        
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root, float('-inf'), float('+inf'))

class Solution_veryfast:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = []
        pre = None
        # the node that we visited just before in our DFS
        # if pre == node.left, then pre.val < node.val
        # if node == pre.right, then pre.val < node.val
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pre != None and pre.val >= root.val:
                return False
            pre = root
            root = root.right
            
        return True
    
#   5
#  / \
# 4   7
node = TreeNode(5)
node.left = TreeNode(4)
node.right = TreeNode(7)

print(Solution().isValidBST(node))
# True