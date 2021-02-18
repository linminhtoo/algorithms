# https://leetcode.com/problems/sum-root-to-leaf-numbers/submissions/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution_recursive_but_unsatisfying:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        def helper(node, s):
            if not node:
                return int(s)
            
            s += str(node.val)
            # don't like how I had to code this in to check for true leaf nodes
            if not node.left and not node.right:
                return helper(node.left, s)
            elif not node.left:
                return helper(node.right, s)
            elif not node.right:
                return helper(node.left, s)
            else:
                left = helper(node.left, s)
                right = helper(node.right, s)
                return left + right
        
        return helper(root, '')

# https://leetcode.com/problems/sum-root-to-leaf-numbers/discuss/41383/Python-solutions-(dfs%2Bstack-bfs%2Bqueue-dfs-recursively).
import collections
class Solution_BFS_queue:
    def sumNumbers2(self, root): # BFS with queue
        deque, res = collections.deque(), 0
        if root:
            deque.append(root)
        while deque:
            node = deque.popleft()
            if not node.left and not node.right:
                res += node.val
            if node.left:
                node.left.val += node.val*10
                deque.append(node.left)
            if node.right:
                node.right.val += node.val*10
                deque.append(node.right)
        return res

class Solution_recursive_global:
    def sumNumbers1(self, root): # DFS recursively 
        self.res = 0 # global var
        self.dfs(root, 0)
        return self.res
    
    def dfs(self, root, path):
        if root:
            if not root.left and not root.right:
                path = path*10 + root.val
                self.res += path
            self.dfs(root.left, path*10+root.val)
            self.dfs(root.right, path*10+root.val)