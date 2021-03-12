from collections import deque
from typing import List
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        # termination condition is when len(visited) == graph.length
        # apparently the above TLE if using a set, so instead, we can use bit mask since we only have 12 nodes (bit mask allows up to 31 nodes)
        
        # need to try all possible starting locations? yes
        N = len(graph)
        all_mask = (1 << N) - 1 # eg if N = 3, 1 << 3 = 1000, 1000 - 1 = 0111
        visited = set()
        queue = deque()
        for i in range(N):
            queue.append((i, 0, 1 << i)) # Tuple[node, dist, visited_mask]
        
        while queue:
            curr_node, curr_dist, curr_mask = queue.popleft()
            # print(curr_node, curr_dist, curr_mask)
            if curr_mask == all_mask:
                return curr_dist
            else:
                for neigh_node in graph[curr_node]:
                    # IMPORTANT! we need to set curr_dist = 0 for storing in the visited set
                    # this will prune cycles, otherwise cycles will never end (since curr_dist keeps increasing by 1)
                    check = (neigh_node, 0, curr_mask | 1 << neigh_node)
                    if check not in visited:
                        visited.add(check)
                        new_tuple = (neigh_node, curr_dist + 1, curr_mask | 1 << neigh_node)
                        queue.append(new_tuple)