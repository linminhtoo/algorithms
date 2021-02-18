import functools 
from typing import List

class Solution_recursive_memo:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        denied = {}
        for i in forbidden:
            denied[i]=True
        visited = {}
        
        @lru_cache(None)
        def solve(position, is_back_jump_again):
            if (position, is_back_jump_again) in visited:   # If the condition is already visited.
                return float('inf')
            else:
                visited[ (position, is_back_jump_again)] = True   # Else add it to visited list
            
            if position == x:   # Reached the required posiiton
                return 0
            
            if position in denied or position > 5998:  
				"""
					If landed in the denied area or went too far from destination
				"""
                return float('inf')
            
            if is_back_jump_again or position-b<0: # If went in negative zone then move ahead only
                return 1 + solve(position+a, False)
            
            return 1 + min(solve(position+a, False), solve(position-b, True))
        
        ans = solve(0, False)
        return ans if ans != float('inf') else -1

class Solution_BFS:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        # Shortest distance to x : min jumps
        forbidden = set(forbidden)
        queue = deque([(0,False)])
        ans = 0
        seen = set()
        seen.add((0,False))
        while queue:
            for _ in range(len(queue)):
                curr, is_last_backward = queue.popleft()
                if curr == x:
                    return ans
                
                # Jump forward
                next_pos = curr + a
                if next_pos not in forbidden and next_pos < 4000 and (next_pos,False) not in seen:
                    queue.append((next_pos, False))
                    seen.add((next_pos, False))
                # Jump backward
                if not is_last_backward:
                    next_pos = curr - b
                    if next_pos >= 0 and next_pos not in forbidden and (next_pos, True) not in seen :
                        queue.append((next_pos,True))
                        seen.add((next_pos, True))
         
                
            ans += 1
        
        return -1