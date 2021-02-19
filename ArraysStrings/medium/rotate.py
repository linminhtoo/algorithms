from typing import List
class Solution:
    def rotate(self, M: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def transpose(M):
            H = len(M)
            W = len(M[0])
            for i in range(H):
                for j in range(i, W):
                    M[i][j], M[j][i] = M[j][i], M[i][j]

        def reverse(M):
            H = len(M)
            W = len(M[0])
            for i in range(H):
                for j in range(W//2):
                    M[i][j], M[i][W-1-j] = M[i][W-1-j], M[i][j]
                    
        transpose(M)
        reverse(M)
        return M