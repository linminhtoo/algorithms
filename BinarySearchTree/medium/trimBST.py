from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# https://leetcode.com/problems/trim-a-binary-search-tree/discuss/1073301/iterative-level-order-logical-queue-general
    #   2
    #  / \
    # 1   3
class Solution_mine_iterative:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
		# use dummy node since we dont know if root will be part of trimmed BST
        dummy = TreeNode('dummy', left=root, right=None)
        
        q = deque([dummy])
        # iterative, level order traversal of nodes
        while q:
            curr = q.popleft()

            if curr.left:
                # for each node, we use BFS to find candidate node to connect as node.left
                # from qns, it is guaranteed that there exists only one such candidate node that is correct
                cands = deque([curr.left])
                found = None # this will be the node to connect as curr.left
                while not found and cands:
                    cand = cands.popleft()

                    if high >= cand.val >= low:
                        found = cand # we found it
                    else:
						# small note: it is possible to incorporate knowledge about BST here, i.e.
						# if cand.val > high and cand.left:
                        if cand.left:
                            cands.append(cand.left)
						# if cand.val < low and cand.right:
                        if cand.right:
                            cands.append(cand.right)
						# however i found addition of these did not improve runtime in practice

                curr.left = found # connect
                if curr.left:
                    q.append(curr.left) # continue in level order traversal
            
            if curr.right:
                # similar to above, we use BFS to find candidate node to connect as node.right
                cands = deque([curr.right])
                found = None # this will be the node to connect as curr.right
                while not found and cands:
                    cand = cands.popleft()

                    if high >= cand.val >= low:
                        found = cand # we found it
                    else:
                        if cand.left:
                            cands.append(cand.left)
                        if cand.right:
                            cands.append(cand.right)

                curr.right = found # connect
                if curr.right:
                    q.append(curr.right)  # continue in level order traversal
        return dummy.left

class Solution_binary_search:
    # smart, bcos you use invariant of BST -> node.left.val <= node.val <= node.right.val
    # TC is O(logN) worst case O(N) bcos on avg we can cut search by half
    # SC is O(1)
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        head = TreeNode(left=root) # Guard Node
        pre, cur = head, head.left 
		# Binary search for low
        while cur:
            if cur.val > low:
                pre = cur
                cur = cur.left
            elif cur.val < low: # trim nodes less than low
                cur = cur.right
                pre.left = cur 
            else:
                cur.left = None
                break
        head.right = head.left # now we dont care about head.left anymore, as it was only checked & modified to meet val > low criteria
        pre, cur = head, head.right
		# Binary search for high
        while cur:
            if cur.val < high:
                pre = cur
                cur = cur.right
            elif cur.val > high: # trim nodes larger than high
                cur = cur.left
                pre.right = cur
            else:
                cur.right = None
                break
        return head.right

class Solution_recursive:
    # TC: O(N), SC: O(N) (due to recursive stack, worst case when BST = linked list)
    # When \text{node.val > high}node.val > high, 
    # we know that the trimmed binary tree must occur to the left of the node.
    # Similarly, when \text{node.val < low}node.val < low, the trimmed binary tree occurs to the right of the node. Otherwise, we will trim both sides of the tree.
    def trimBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        """
        def trim(node):
            if not node:
                return None
            elif node.val > high:
                return trim(node.left)
            elif node.val < low:
                return trim(node.right)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node

        return trim(root)