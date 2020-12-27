from typing import List
# https://leetcode.com/problems/jump-game-iv/
# https://leetcode.com/problems/jump-game-iv/discuss/502711/Python-Simple-Solution-with-Explanations 
# very similar approach
class Solution_mine_BFS: # 620 ms, beats 33%
    def minJumps(self, A: List[int]) -> int:
        hashmap = {} # key = A[i], value = List[idxs]
        for i, a in enumerate(A):
            if a in hashmap:
                hashmap[a].append(i)
            else:
                hashmap[a] = [i]
        
        stack = deque()
        stack.append((A[0], 0, 0)) # (value, distance, index)
        visited = [False for _ in range(len(A))]
        visited[0] = True
        while stack:
            now, dist, idx = stack.popleft()
            if idx == len(A) - 1: # reached the end of A
                return dist
            
            for move in [+1, -1]:
                next_idx = idx + move
                if 0 <= next_idx < len(A) and not visited[next_idx]:
                    stack.append((A[next_idx], dist+1, next_idx))
                    visited[next_idx] = True
            
            if now in hashmap:
                same = hashmap.pop(now) # idxs of numbers identical to now
                for next_idx in same:
                    if not visited[next_idx]:
                        visited[next_idx] = True
                        stack.append((A[next_idx], dist+1, next_idx))