# https://leetcode.com/problems/unique-paths-iii/submissions/
# good practice for backtracking!
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.res, steps = 0, 1
        # use of "global" class attribute to track successful paths
        # steps = 1 bcos we start from starting point so we already took 1 step in getting to starting point (use pen & paper to check)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    x, y = i, j
                elif grid[i][j] == 0:
                    steps += 1
        
        def dfs(x, y, steps):
            if not (0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] >= 0): return
            if grid[x][y] == 2:
                self.res += (steps == 0)
                return
            
            grid[x][y] = -2 # temporarily set this block as obstacle to avoid repeated visits
            dfs(x+1, y, steps-1)
            dfs(x-1, y, steps-1)
            dfs(x, y+1, steps-1)
            dfs(x, y-1, steps-1)
            grid[x][y] = 0 # reset to non-obstacle, i.e. backtracking to allow parallel recursive branches to access
            
        dfs(x, y, steps)
        return self.res