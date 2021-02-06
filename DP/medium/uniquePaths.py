# https://leetcode.com/problems/unique-paths/submissions/
# https://leetcode.com/problems/unique-paths/discuss/182143/Recursive-memoization-and-dynamic-programming-solutions

# for recurisve, time complexity is O(2^(n+m))
# bcos u have to traverse whole of m, and then, after that, still need to traverse whole of n
# each traversal is a split of the parent node into 2 children, hence 2**
# space complexity is just height of recursive stack, which is O(log(n+m))
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for _ in range(n)] for _ in range(m)]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
        return dp[m-1][n-1]