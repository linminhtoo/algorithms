from typing import List
# https://leetcode.com/problems/range-sum-query-2d-immutable/submissions/
class NumMatrix: # rect_sums, idea is to break down area into 4 rectangles starting from origin
    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            self.sums = None
        else:
            # need to pad w/ row & col of 0's
            self.sums = [[0 for _ in range(len(matrix[0])+1)] for _ in range(len(matrix)+1)]
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    # bcos of padding, LHS is [i+1][j+1]
                    self.sums[i+1][j+1] = matrix[i][j] + self.sums[i][j+1] + self.sums[i+1][j] - self.sums[i][j] # to subtract doubly counted area-sum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if not self.sums:
            return 0
        else:
            return self.sums[row2+1][col2+1] + self.sums[row1][col1] - self.sums[row1][col2+1] - self.sums[row2+1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)