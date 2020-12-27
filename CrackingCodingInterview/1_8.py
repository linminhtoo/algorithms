from typing import List

class Solution:
    @staticmethod
    def zero_matrix(matrix: List[List[int]]):
        rows_to_change = set()
        cols_to_change = set()

        for row_idx, row in enumerate(matrix):
            for col_idx, col in enumerate(matrix[row_idx]):
                if matrix[row_idx][col_idx] == 0:
                    for c_idx, c in enumerate(matrix[row_idx]):
                        cols_to_change.add(c_idx)

                        # matrix[row_idx][c_idx] = 0
                    for r_idx, r in enumerate(matrix):
                        rows_to_change.add(r_idx)
                        # matrix[r_idx][col_idx] = 0
                
        return matrix

if __name__ == '__main__':
    print(Solution.zero_matrix([[0, 1, 2], [2, 3, 4], [5, 6, 7]]))