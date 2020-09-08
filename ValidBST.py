class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left
    
class Solution(object):
    def _isValidBSTHelper(self, n, low, high):
        if not n:
            return True
        val = n.val
        if ((val > low and val < high) and 
            self._isValidBSTHelper(n.left, low, n.val) and
            self._isValidBSTHelper(n.right, n.val, high)):
            return True
        return False
    
    def isValidBST(self, n):
        return self._isValidBSTHelper(n, float('-inf'), float('inf'))
        
#   5
#  / \
# 4   7
node = Node(5)
node.left = Node(4)
node.right = Node(7)

print(Solution().isValidBST(node))
# True