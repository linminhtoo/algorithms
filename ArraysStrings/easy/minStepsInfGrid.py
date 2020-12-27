# https://www.interviewbit.com/problems/min-steps-in-infinite-grid/
from typing import List
class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return an integer
    def coverPoints(self, A: List[int], B: List[int]) -> int:
        i = 0
        total = 0
        while i + 1 <= len(A) - 1:
            total += max(
                    abs(A[i+1] - A[i]),
                    abs(B[i+1] - B[i])
                )
            i += 1
        return total