# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution_DFS_recursive: 
    # time complexity O(N) worst case, but we often stop before that if d < max_height
    # space complexity is O(d) worst case, the height of recursive stack is at most d
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        dummy = TreeNode(val='dummy')
        dummy.left = root
        
        # curr_node + prev_node
        # do DFS, keep track of current depth, starting from 0 at dummy
        # when curr_depth == d, we need to insert TreeNode(val=v) between prev_node & curr_node
        # for leftmost branch, this would be
        # new = TreeNode(val=v), prev_node.left = new, new.left = curr_node
        # need to remember the direction from prev_node to curr_node
        # was it left, or right
        
        # it is ok for curr_node to be None, we still need to build it, but prev_node must not be None
        
        def DFS(curr, prev, depth, link):
            if depth == d:
                new = TreeNode(val=v)
                if link == 'l':
                    prev.left = new
                    new.left = curr
                else:
                    prev.right = new
                    new.right = curr
            else:
                if curr:
                    DFS(curr.left, curr, depth+1, 'l')
                    DFS(curr.right, curr, depth+1, 'r')          
            
        DFS(dummy, None, 0, 'l')
        return dummy.left

from collections import deque
class Solution_stack_BFS:
    # time complexity O(N) worst case
    # space complexity O(d), this is the maximum size our queue will have
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        dummy = TreeNode(val='dummy')
        dummy.left = root
        
        q = deque([dummy])
        depth = 0
        while q and depth < d - 1:
            level_cnt = len(q)
            while level_cnt:
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                level_cnt -= 1
            depth += 1
        
        while q:
            curr = q.popleft()
            temp = curr.left
            new = TreeNode(val=v)
            curr.left = new
            curr.left.left = temp
            
            temp = curr.right
            new = TreeNode(val=v)
            curr.right = new
            curr.right.right = temp
        
        return dummy.left