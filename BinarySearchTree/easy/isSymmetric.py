# https://leetcode.com/problems/symmetric-tree/solution/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution_recursive:
    # recursive, by comparing two copies of the tree
    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(t1, t2):
            # compare mirror image of tree against itself
            if not t1 and not t2: return True
            if not t1 or not t2: return False
            
            return (
                t1.val == t2.val and \
                helper(t1.left, t2.right) and \
                helper(t1.right, t2.left)
            )
        return helper(root, root)

from collections import deque
class Solution_iterative:
    # level order traversal
    # just need to handle Null nodes carefully
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        q = deque([root])
        while q:
            level_count = len(q)
            level_nodes = []
            while level_count:
                node = q.popleft()
                if node:
                    level_nodes.append(node.val)

                    if node.left:
                        q.append(node.left)
                    else:
                        q.append(None)
                    if node.right:
                        q.append(node.right)
                    else:
                        q.append(None)
                else:
                    level_nodes.append(None)
                level_count -= 1
            if level_nodes != level_nodes[::-1]:
                return False
        return True