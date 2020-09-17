class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# recursive 1
class Solution(object):
    def rangeSumBST(self, root, L, R):
        def dfs(node):
            if node:
                if L <= node.val <= R:
                    self.ans += node.val
                if L < node.val:
                    dfs(node.left)
                if node.val < R:
                    dfs(node.right)

        self.ans = 0
        dfs(root)
        return self.ans

# recursive 2
class recursive2_Solution(object):
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        elif root.val < L:
            return self.rangeSumBST(root.right, L, R)
        elif root.val > R:
            return self.rangeSumBST(root.left, L, R)
        return root.val + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)

# iterative 
class iterative_Solution(object):
    def rangeSumBST(self, root, L, R):
        ans = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if L <= node.val <= R:
                    ans += node.val
                if L < node.val:
                    stack.append(node.left)
                if node.val < R:
                    stack.append(node.right)
        return ans

# inorder traversal
def inorder(self, root, value, L, R):
    if root:
        value = self.inorder(root.left, value, L, R)
        # stop traversing once we reach a node greater than R
        if root.val > R:
            return value
        elif root.val >= L:
            value += root.val
        value = self.inorder(root.right, value, L, R)
        
    return value