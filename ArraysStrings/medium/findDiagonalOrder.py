from typing import List
class Solution_mine:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        M, N = len(matrix), len(matrix[0])
        if M == 1:
            return [num for num in matrix[0]]
        if N == 1:
            return list(*zip(*matrix))
        # pad 1 layer
        A = [[None] * (M+2)]
        for row in matrix:
            A.append([None] + row + [None])
        A.append([[None] * (M+2)])
        M, N = M + 2, N + 2
        # initial direction & position
        dr, dc = -1, +1
        r, c = 2, 0
        out = []
        while len(out) < (M-2) * (N-2):
            r += dr
            c += dc
            if 1 <= r < M - 1 and 1 <= c < N - 1:
                out.append(A[r][c])
                if (dr, dc) == (+1, 0): # was going down
                    dr, dc = +1, -1
                elif (dr, dc) == (0, +1): # was going right
                    dr, dc = -1, +1
            else: # r or c or both out of range
                if (dr, dc) == (-1, +1): # was going up-right:
                    dr, dc = +1, 0 # move down
                elif (dr, dc) == (+1, -1): # was going down-left
                    dr, dc = 0, +1 # move right
                elif (dr, dc) == (+1, 0): # was going down
                    dr, dc = +1, -1 # move down-left
                elif (dr, dc) == (0, +1): # was going right
                    dr, dc = -1, +1 # move up-right
        return out

# The key here is to realize that the sum of indices on all diagonals are equal.
# [1,2,3]
# [4,5,6]
# [7,8,9]
# 2, 4 are on the same diagonal, and they share the index sum of 1. (2 is matrix[0][1] and 4 is in matrix[1][0]).
# 3,5,7 are on the same diagonal, and they share the sum of 2. (3 is matrix[0][2], 5 is matrix[1][1], and 7 is matrix [2][0]).
class Solution_sum_idx_diagonal_equal:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        d={} # in python 3.6+ dictionaries are ordered
		#loop through matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
				#if no entry in dictionary for sum of indices aka the diagonal, create one
                if i + j not in d:
                    d[i+j] = [matrix[i][j]]
                else:
				#If you've already passed over this diagonal, keep adding elements to it!
                    d[i+j].append(matrix[i][j])
		# we're done with the pass, let's build our answer array
        ans= []
		#look at the diagonal and each diagonal's elements
        for entry in d.items():
			#each entry looks like (diagonal level (sum of indices), [elem1, elem2, elem3, ...])
			#snake time, look at the diagonal level
            if entry[0] % 2 == 0:
				#Here we append in reverse order because its an even numbered level/diagonal. 
                [ans.append(x) for x in entry[1][::-1]]
            else:
                [ans.append(x) for x in entry[1]]
        return ans