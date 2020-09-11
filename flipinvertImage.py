# https://leetcode.com/problems/flipping-an-image/submissions/
# Runtime: 52 ms, faster than 75.63% of Python3 online submissions for Flipping an Image.
# Memory Usage: 13.9 MB, less than 53.42% of Python3 online submissions for Flipping an Image.

from Typing import List

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        K = self.flip(A)
        A = self.invert(K)
        return A    
    
    def flip(self, A: List[List[int]]) -> List[List[int]]:
        N = len(A)
        for x in range(0, N):
            for y in range(0, int(N/2)):
                temp = A[x][y]
                A[x][y] = A[x][N-y-1]
                A[x][N-y-1] = temp
        return A 
    
    def invert(self, A: List[List[int]]) -> List[List[int]]:
        N = len(A)
        for x in range(0, N):
            for y in range(0, N):
                if A[x][y] == 1:
                    A[x][y] = 0
                else:
                    A[x][y] = 1
        
        return A