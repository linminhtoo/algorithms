class Solution:
    def numTrees(self, n: int) -> int:
        # BST invariant: node.left.val < node.val < node.val.right (since values must be unique)
        # time complexity should be O(N^2) bcos we have first loop for idx in range(N) as top level
        # then the helper function needs to count the smaller subtrees, for subtree with N-1 nodes we need to loop N-1 times there again
        # so it is N + N-1 + N-2 + ... + 1 = O(N^2)
        def helper(i, memo):
            if i == 0:
                return 1
            
            if i in memo:
                return memo[i]
            else:
                res = 0
                for idx in range(i):
                    left = helper(idx, memo) # number of subtrees on left, that can be made with idx nodes
                    right = helper(i - idx - 1, memo)  # number of subtrees on right, that can be made with i - idx - 1 nodes
                    # both left subtree & right subtree will add up to i - 1 nodes, since we use up 1 node for the root
                    res += left * right # we can have any combination of left subtree & right subtree
                memo[i] = res
                return res
        return helper(n, {})
            