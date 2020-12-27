class Solution:
    @staticmethod
    def unique_paths(m: int, n: int):
        grid = [[0 for i in range(n+1)] for j in range(m+1)]
        grid[1][1] = 1

        for row_idx in range(1, m+1):
            for col_idx in range(1, n+1): 
                grid[row_idx][col_idx] += grid[row_idx][col_idx-1] + grid[row_idx-1][col_idx]

        return grid[m][n]

if __name__ == '__main__':
    print(Solution.unique_paths(3, 7))
    print(Solution.unique_paths(4, 8))
    print(Solution.unique_paths(1, 2))

