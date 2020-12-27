
from typing import List
# https://leetcode.com/problems/max-increase-to-keep-city-skyline/s
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        skyline_vert = [[0] * len(grid[0])] * len(grid)
        skyline_hori = [[0] * len(grid[0])] * len(grid)
        
        for row_idx in range(len(grid)):
            skyline_hori[row_idx] = [max(grid[row_idx])] * len(grid[0])
            
        vert_nums = [] # transpose grid
        for col_idx in range(len(grid[0])):
            this_col = []
            for row_idx in range(len(grid)):
                this_col.append(grid[row_idx][col_idx])
            vert_nums.append(this_col)
                
        for col_idx in range(len(grid[0])):
            for row_idx in range(len(grid)):
                skyline_vert[row_idx][col_idx] = max(vert_nums[col_idx])
                
        maxed = [[0] * len(grid[0])] * len(grid)
        maxed_diff = 0
        for row_idx in range(len(grid)):
            for col_idx in range(len(grid[0])):
                maxed[row_idx][col_idx] = min(skyline_vert[row_idx][col_idx], skyline_hori[row_idx][col_idx])
            maxed_diff += sum(maxed[row_idx]) - sum(grid[row_idx])
            
        return maxed_diff