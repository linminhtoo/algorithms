# https://leetcode.com/problems/unique-paths-ii/submissions/
# very similar to uniquePaths.py
class Solution:
    def uniquePathsWithObstacles(self, O: List[List[int]]) -> int:
        m, n = len(O), len(O[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        blocked = False
        for j in range(n):
            if O[0][j] == 1:
                blocked = True
            if not blocked:
                dp[0][j] = 1
        
        blocked = False
        for i in range(m):
            if O[i][0] == 1:
                blocked = True
            if not blocked:
                dp[i][0] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                if O[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
        return dp[m-1][n-1]
        
class Solution_model:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # If the starting cell has an obstacle, then simply return as there would be
        # no paths to the destination.
        if obstacleGrid[0][0] == 1:
            return 0

        # Number of ways of reaching the starting cell = 1.
        obstacleGrid[0][0] = 1

        # Filling the values for the first column
        for i in range(1,m):
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1)

        # Filling the values for the first row        
        for j in range(1, n):
            obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j-1] == 1)

class Solution_dfs:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        brute force, bottom-up recursively with memorization
        - intuitively go through all the path with i+1 OR j+1
        - count the path which reaches to the destination coordinate (m, n)
        - cache the count of the coordinates which we have calculated before
        - if the current grid, grid[i][j], is blocked, tell its parent that this way is blocked by return 0
        - sum up all the coordinates' count

        Time    O(row*col) since we cache the intermediate coordinates, we wont go through the visited coordinates again
        Space   O(row*col) depth of recursions
        """
        if len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
            return 0
        seen = {}
        return self.dfs(obstacleGrid, 0, 0, len(obstacleGrid)-1, len(obstacleGrid[0])-1, seen)

    def dfs(self, grid, i, j, m, n, seen):
        key = str(i)+","+str(j)
        if key in seen:
            return seen[key]
        if i == m and j == n:
            if grid[i][j] == 1:
                return 0
            return 1
        elif i > m or j > n:
            return 0
        if grid[i][j] == 1:
            seen[key] = 0
            return 0
        left = self.dfs(grid, i+1, j, m, n, seen)
        right = self.dfs(grid, i, j+1, m, n, seen)
        seen[key] = left + right
        return left + right