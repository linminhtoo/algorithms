from typing import List
class Solution:
    def findOrder(self, C: int, P: List[List[int]]) -> List[int]:
        # g[0] == 0, so S = [0]
        # curr = S.pop() = 0
        # for neigh in graph[0] --> [1, 2]
        # g[1] -= 1, g[2] -= 1 --> g[1] = 0 and g[2] = 0
        # S.append(1), S.append(2) --> S = [1, 2]
        # i think we do want to use a queue here to make sure all the low level courses are finished first --> actually no, I think it doesn't matter!
        
        graph = [[] for _ in range(C)]
        g = [0] * C
        for v, u in P:
            graph[u].append(v)
            g[v] += 1
        
        S = [i for i in range(C) if g[i] == 0]
        res = S.copy()
        while S:
            curr = S.pop()
            for neigh in graph[curr]:
                g[neigh] -= 1
                if g[neigh] == 0:
                    S.append(neigh)
                    res.append(neigh)
        if not any(g):
            return res
        else:
            return []