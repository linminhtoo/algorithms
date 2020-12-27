# https://leetcode.com/problems/sparse-matrix-multiplication/ 
from typing import List
class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        result = [[None for _ in range(len(B[0]))] for _ in range(len(A))]

        for row_result_index, row_A in enumerate(A):
            for col_result_index, _ in enumerate(B[0]):
                cur_sum = 0
                for col_index_A, _ in enumerate(row_A):
                    cur_sum += (B[col_index_A][col_result_index] * row_A[col_index_A])

                result[row_result_index][col_result_index] = cur_sum

        return result