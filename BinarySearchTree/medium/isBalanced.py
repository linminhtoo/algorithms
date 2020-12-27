# https://leetcode.com/submissions/detail/433325047/?from=explore&item_id=3577
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        def helper(node):
            if not node:
                return 0,True
            
            l_height,l_corr = helper(node.left)
            if not l_corr:
                return -1,False
            
            r_height,r_corr = helper(node.right)
            if not r_corr:
                return -1,False
            
            return (1 + max(l_height,r_height), abs(l_height - r_height) <= 1)
        
        return helper(root)[1]

class Solution_faster(object):
    def isBalanced(self, root):
        def check(root):
            if not root:
                return 0
            
            left = check(root.left)
            if left == -1:
                return -1
            right = check(root.right)
            if right == -1:
                return -1
            
            if abs(left - right) > 1:
                return -1
            return max(left, right) + 1
        
        return check(root) != -1
