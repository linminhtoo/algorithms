# leetcode is premium problem
# see https://www.geeksforgeeks.org/minimum-steps-reach-target-knight/
# https://www.hackerrank.com/challenges/knightl-on-chessboard/problem <-- slightly harder version of the same problem (SCROLL DOWN)
# BFS
class Cell: # don't have to use this, can just use a tuple also (x, y, dist)
    def __init__(self, x: int, y: int, dist: int):
        self.x = x
        self.y = y
        self.dist = dist
from typing import Tuple
from collections import deque
class Solution:
    def inBoard(self, x: int, y: int) -> bool:
        return (0 <= x < 8) and (0 <= y < 8)

    def minKnightMoves(self, knight_pos: Tuple[int, int],
                            target_pos: Tuple[int, int]) -> int:
        dirs = [
            (1, 2),
            (2, 1),
            (-1, -2),
            (-2, -1),
            (-1, 2),
            (2, -1),
            (1, -2),
            (-2, 1)
        ]

        queue = deque()
        queue.append(Cell(knight_pos[0], knight_pos[1], 0))

        visited = [[False] * 8 for _ in range(8)]
        visited[knight_pos[0]][knight_pos[1]] = True
        while queue:
            now = queue.popleft()
            if (now.x, now.y) == target_pos:
                return now.dist 
            
            for i in range(8):
                next_x = now.x + dirs[i][0]
                next_y = now.y + dirs[i][1]
                if self.inBoard(next_x, next_y):
                    if not visited[next_x][next_y]:
                        visited[next_x][next_y] = True
                        queue.append(Cell(next_x, next_y, now.dist + 1))

# https://www.hackerrank.com/challenges/knightl-on-chessboard/problem
class Solution_hackerrank_mine_passall:
    def knightlOnAChessboard(self, n: int):
        out = [[0]*(n-1) for _ in range(n-1)]
        for i in range(1, n):
            for j in range(1, n):
                if out[j-1][i-1] != 0: # output array is symmetric
                    out[i-1][j-1] = out[j-1][i-1]
                else:
                    out[i-1][j-1] = makeMove(n, i, j)
        return out
    
    @staticmethod
    def inBoard(n: int, x: int, y: int) -> bool:
        return (0 <= x < n) and (0 <= y < n)
    
    @staticmethod
    def makeMove(n: int, a: int, b: int) -> int:
        dirs = [
            (a, b),
            (b, a),
            (-a, b),
            (b, -a),
            (a, -b),
            (-b, a),
            (-a, -b),
            (-b, -a)
        ]
        queue = deque()
        queue.append(Cell(0, 0, 0))

        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True
        while queue:
            now = queue.popleft()
            if (now.x, now.y) == (n-1, n-1):
                return now.dist 
            
            for i in range(8):
                next_x = now.x + dirs[i][0]
                next_y = now.y + dirs[i][1]
                if inBoard(n, next_x, next_y):
                    # exploit symmetry of chess board (start from topleft, end at bottomright)
                    # ONLY works in this special problem! (not for the generic leetcode problem above)
                    # offers small speedup
                    if visited[next_y][next_x]: 
                        visited[next_x][next_y] = True
            
                    if not visited[next_x][next_y]:
                        visited[next_x][next_y] = True
                        queue.append(Cell(next_x, next_y, now.dist + 1))
        return -1