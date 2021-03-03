# https://leetcode.com/problems/balance-a-binary-search-tree/submissions/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # my solution, but can be optimized for space complexity
    # 1) store TreeNode object, not values in self.res
    # 2) in build, just connect these TreeNode objects
    def balanceBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        # do an in-order traversal, node.left --> node --> node.right
        # self.res will ALWAYS be sorted in ascending order
        # then build a new BST that is balanced
        self.res = []
        def inorder(node): # O(N) time & extra space
            if node:
                inorder(node.left)
                self.res.append(node.val)
                inorder(node.right)
        inorder(root) # [1, 2, 3, 4]
        def build(node, low_idx, high_idx):
            if low_idx > high_idx:
                return
            
            new_idx = (low_idx + high_idx) // 2
            child = self.res[new_idx]
            if node.val < child:
                node.right = TreeNode(val=child)
                build(node.right, low_idx, new_idx-1)
                build(node.right, new_idx+1, high_idx)
            else:
                node.left = TreeNode(val=child)
                build(node.left, low_idx, new_idx-1)
                build(node.left, new_idx+1, high_idx)
        
        dummy = TreeNode(val=0)
        build(dummy, 0, len(self.res)-1) 
        # should be O(N) time also since we need to touch every node once
        # height of recursive stack is O(logN)
        # no extra space? since we are just connecting existing TreeNodes, but not sure if 
        # we need extra space to store different values of low_idx, new_idx, high_idx etc for each call
        # in which case, we need O(2N) extra space since we need to call build() twice for each node
        return dummy.right

class Solution_spaceoptimized:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.res = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            self.res.append(node)
            inorder(node.right)
        
        def buildBst(start, end):
            if start > end:
                return None
            mid = start + (end - start) // 2
            root = self.res[mid]
            root.left = buildBst(start, mid - 1)
            root.right = buildBst(mid + 1, end)
            return root

        if not root:
            return None
        inorder(root)
        return buildBst(0, len(self.res) - 1)