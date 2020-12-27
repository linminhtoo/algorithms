# should be MEDIUM 
# https://leetcode.com/problems/increasing-order-search-tree/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution_recursion:
    # but not easy to think about
    # idea is to connect root.right = nxt
    # next node info is passed down the tree from root node
    def increasingBST(self, root: TreeNode, nxt=None) -> TreeNode:
        if not root:
            return nxt
        res = self.increasingBST(root.left, root)
        root.left = None
        root.right = self.increasingBST(root.right, nxt)
        return res # the bottom leftmost node of entire BST

class Solution_inorder_traversal:
    # relink on the spot
    def increasingBST(self, root):
        def inorder(node):
            if node:
                inorder(node.left)
                node.left = None
                self.cur.right = node
                self.cur = node
                inorder(node.right)

        ans = self.cur = TreeNode(None)
        inorder(root)
        return ans.right

class Solution_mine_DFS:
    def increasingBST(self, root: TreeNode) -> TreeNode: 
        def dfs(node, nodes):
            if not node:
                return -1, nodes
            left, left_nodes = dfs(node.left, nodes)
            if left == -1:
                left_nodes = [TreeNode(val=node.val)]
            else:
                left_nodes.append(TreeNode(val=node.val))
            _, right_nodes = dfs(node.right, [])
            return 1, left_nodes + right_nodes
        
        _, nodes = dfs(root, [])
        i = 0
        while i + 1 <= len(nodes) - 1:
            nodes[i].left = None
            nodes[i].right = nodes[i+1]
            i += 1
        return nodes[0] # new root