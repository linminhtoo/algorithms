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