# https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms)
# use of master's theorem is interesting

# anyway for an inefficient solution, it is O(NlogN) assuming balanced binary tree
# bcos O(N) to check depth starting from a particular node, and 
# O(logN) bcos problem size is halved each time we go down one level
# T(N) = 2 * T(N/2) + O(N)

# but if it is a perfectly unbalanced i.e. linkedlist, 
# then O(N^2) bcos T(N) = N + N-1 + N-2 + ... + 2 + 1 etc.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import defaultdict
class Solution_iterative:        
    def isBalanced(self, root: TreeNode) -> bool:
        # almost identical to iterative, post order traversal
        # just need to check depth & store it in dictionary
        stack = []
        depths = defaultdict(int)
        curr, last = root, None
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack[-1] # peek
                if not curr.right or last == curr.right:
                    curr = stack.pop()
                    left = depths[curr.left]
                    right = depths[curr.right]
                    if abs(left - right) > 1:
                        return False
                    depths[curr] = 1 + max(left, right)
                    last = curr
                    curr = None
                else:
                    curr = curr.right
        return True

class Solution_recursive:
    # just realized h argument is completely redundant
    def helper(self, node, h, balanced):
        if not node:
            return h, True
        if not balanced:
            return 0, False
        
        l_h, l_bal = self.helper(node.left, h, balanced)
        r_h, r_bal = self.helper(node.right, h, balanced)
        
        if not l_bal or not r_bal:
            return 0, False
        if abs(l_h - r_h) <= 1:
            return max(l_h, r_h)+1, True
        else:
            return 0, False
    
    def isBalanced(self, root: TreeNode) -> bool:
        return self.helper(root, 0, True)[1]

    # conceptually identical to mine, just that no need to use balanced boolean flag
    # if depthsofar == -1, it means node is not balanced already
class Solution_recursive_simpler:
    def helper(self, node):
        if not node:
            return 0
        
        left = self.helper(node.left)
        if left == -1:
            return -1
        right = self.helper(node.right)
        if right == -1:
            return -1
        
        if abs(left - right) > 1:
            return -1
        else:
            return 1 + max(left, right)
        
    def isBalanced(self, root: TreeNode) -> bool:
        return self.helper(root) != -1