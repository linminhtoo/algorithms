# https://leetcode.com/problems/number-of-provinces/

# Union Find question, should I use it?
from typing import List
class Solution:
    # DFS solution, should be O(N^2) bcos O(N) nodes + O(N) DFS for each (altho can be faster)
    # beats 99%
    # https://leetcode.com/problems/number-of-provinces/discuss/101349/Python-Simple-Explanation
    def findCircleNum(self, A: List[List[int]]) -> int:
        M = len(A)
        res = 0
        seen = set()
        def dfs(node):
            for nei, adj in enumerate(A[node]):
                if adj and nei not in seen:
                    seen.add(nei)
                    dfs(nei)
        
        for i in range(M):
            if i not in seen:
                seen.add(i)
                dfs(i)
                res += 1
        
        return res

class Solution_UF:
    # unify(p, q)
    # find(p)
    # numcomponents()

    # https://www.youtube.com/watch?v=0jNmHPfA_yE
    # https://github.com/williamfiset/Algorithms/blob/master/src/main/java/com/williamfiset/algorithms/datastructures/unionfind/UnionFind.java
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        def find_iterative(node): # with path compression
            # find root
            root = node
            while root != circles[root]:
                root = circles[root]
            
            while root != node:
                # path compression
                next = circles[node]
                circles[next] = root # all must point to same root
                node = next
            
            return root

        def find(node):
            # find root of a node + path compression (recursively)
            if circles[node] == node: return node
            root = find(circles[node])
            circles[node] = root
            return root
        
        n = len(M)
        circles = {x:x for x in range(n)}
        num = n
        for i in range(n):
            for j in range(i, n):
                if i != j and M[i][j] == 1 and find(i) != find(j):
                    circles[find(i)] = find(j)   
                    
        return sum([1 for k, v in circles.items() if k == v])