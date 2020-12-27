from typing import List
class Solution_concise:
    def numRookCaptures(self, board):
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    x0, y0 = i, j
        res = 0
        for i, j in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            x, y = x0 + i, y0 + j
            while 0 <= x < 8 and 0 <= y < 8:
                if board[x][y] == 'p': res += 1
                if board[x][y] != '.': break
                x, y = x + i, y + j
        return res

class Solution_one_liner:
    def numRookCaptures(self, A):
        return sum(''.join(r).replace('.', '').count('Rp') for r in A + zip(*A) for r in [r, r[::-1]])

class Solution_mine:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # locate da rook
        found = False
        for row_idx in range(len(board)):
            if found:
                break
            for col_idx in range(len(board[0])):
                if found:
                    break
                if board[row_idx][col_idx] == 'R':
                    row, col = row_idx, col_idx
                    found = True
        count = 0
        # check up
        col_idx = col
        for row_idx in range(row-1, -1, -1):
            piece = board[row_idx][col_idx]
            if piece == '.':
                continue
            elif piece == 'p':
                count += 1
                break
            else: # piece == 'B'
                break
        # check right
        row_idx = row
        for col_idx in range(col+1, len(board[0]), 1):
            piece = board[row_idx][col_idx]
            if piece == '.':
                continue
            elif piece == 'p':
                count += 1
                break
            else:
                break
        # check down
        col_idx = col
        for row_idx in range(row+1, len(board), 1):
            piece = board[row_idx][col_idx]
            if piece == '.':
                continue
            elif piece == 'p':
                count += 1
                break
            else:
                break
        # check left
        row_idx = row
        for col_idx in range(col-1, -1, -1):
            piece = board[row_idx][col_idx]
            if piece == '.':
                continue
            elif piece == 'p':
                count += 1
                break
            else:
                break
        return count

class Solution_fastest:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        #Rook's initial position
        rr = -1
        rc = -1
        #find](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array) Rook's position
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'R':
                    rr, rc = r, c
                    break
        def goto(r,c,direction):
            while c >=0 and c < len(board[0]) and r >=0 and r < len(board):
                if board[r][c] == 'p':
                    return 1
                if board[r][c] == 'B':
                    break
                c-= direction == 'L'
                c += direction == 'R'
                r -= direction == 'U'
                r += direction == 'D'
            return 0       
        return goto(rr,rc,'L') + goto(rr,rc,'R')+goto(rr,rc,'U')+goto(rr,rc,'D')