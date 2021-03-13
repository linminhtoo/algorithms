# https://leetcode.com/problems/course-schedule/discuss/1097667/Super-Simple-Python-Solution-beats-99.9
from typing import List
class Solution_indegree_topological_sort:
    def canFinish(self, C: int, P: List[List[int]]) -> bool:
        # if a cycle is present we cannot take at least one of the courses, so return False immediately
        # assume no cycle --> check if we can find an origin that does not need any prerequisites
        # from these origin(s), we need to visit all courses
        # there is no need to check for missing link. if a link is missing, it just means we can start again from the other node (it has 0 prerequisites)
        # so, the condition to satisfy is just that there can be no cycles in the graph
        
        # think we need to build the adjacency list from P
        # e.g. [1,0] --> 0 => 1 --> adj list [[1], []]
        
        # every time we reach a new node, we need to checkcycles()? yes
        
        # or we need to do some topological sorting?
        
        # use g[v] to denote in-degree of each node (aka no. of prereqs)
        # this is TOPOLOGICAL SORTING (KAHN'S ALGORITHM)
        graph = [[] for _ in range(C)]
        g = [0] * C
        for v, u in P:
            graph[u].append(v)
            g[v] += 1
        
        S = [i for i in range(C) if g[i] == 0] # not sure if stack or queue really matters here
        while S:
            curr = S.pop() # this contributes to O(|V|)
            for neigh in graph[curr]: 
                # only checks neighbours of current course (the courses that curr is a prereq of)
                # this contributes to O(|E|)
                g[neigh] -= 1
                if g[neigh] == 0: # all pre-reqs have been visited
                    S.append(neigh)
                    
        return not any(g) # so, total time complexity is O(|V|+|E|)

class Solution: # topological sort, but not using indegree counts
    # is significantly slower than above method
    # bcos here, we have to check every edge in the graph, for every node, so O(|V|*|E|)
    # should use graph dictionary of {prereq: [courses_the_prereq_leads_to]}
    # this will speed it up significantly (should be similar to above)
    def canFinish(self, C: int, P: List[List[int]]) -> bool:
        graph = {c: {} for c in range(C)}
        for c, p in P:
            graph[c][p] = True # sort of an adjacency dictionary
        
        S = []
        for c in range(C):
            if not graph[c]:
                S.append(c)
        
        # print(S, graph, C, P) # [0] {0: {}, 1: {0: True}} 2 [[1, 0]]
        count = 0
        while S:
            curr = S.pop()
            count += 1
            for course, prereqs in graph.items():
                if curr in prereqs:
                    del prereqs[curr]
                    if len(prereqs) == 0:
                        S.append(course)
        return count == C
                