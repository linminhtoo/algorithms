from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        self.results = []

        def helper(cur_node, height, col_index):
            if not cur_node:
                return

        self.results.append([cur_node.val, height, col_index])
        helper(cur_node.left, height + 1, col_index - 1)
        helper(cur_node.right, height + 1, col_index + 1)

        # Process results
        offset = -(min(self.results, key = lambda x: x[2]))
        self.results.sort(key = lambda: x[2])

# BFS      
from collections import defaultdict, deque 
class BFS_Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        columnTable = defaultdict(list)
        queue = deque([(root, 0)])

        while queue:
            node, column = queue.popleft()

            if node is not None:
                columnTable[column].append(node.val)
                
                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))
                        
        return [columnTable[x] for x in sorted(columnTable.keys())]