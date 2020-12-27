from typing import List
# https://leetcode.com/problems/spiral-matrix-ii/submissions/
class Solution_mine:
    def generateMatrix(self, n: int) -> List[List[int]]:
        curr_num = 1
        out = [[0 for _ in range(n)] for _ in range(n)] # cannot use [[0] * n] * n, all rows change tgt 
        # prep for 1st iter (cross top row)
        max_len, r_or_c = n, 1
        now, other = list(range(0, n)), 0
        now_counter = 1
        # prep prev_r for 2nd iter (descend rightmost col)
        prev_r = list(range(0, n))[::-1]
        while curr_num <= n ** 2: 
            if r_or_c % 2 == 0: # travel col
                out[now[now_counter-1]][other] = curr_num
            else: # travel row
                out[other][now[now_counter-1]] = curr_num
            curr_num += 1
            now_counter += 1
            if now_counter - 1 >= max_len:
                r_or_c += 1
                now_counter = 1
                other = now[-1]
                if r_or_c % 2 == 0:
                    max_len -= 1
                    prev_c = now[:]
                    now = prev_r[::-1][1:][:]
                else: # no change to max_len
                    prev_r = now[:]
                    now = prev_c[::-1][1:][:]
        return out

# ||  =>  |9|  =>  |8|      |6 7|      |4 5|      |1 2 3|
#                  |9|  =>  |9 8|  =>  |9 6|  =>  |8 9 4|
#                                      |8 7|      |7 6 5|
class Solution_inside_out: # https://leetcode.com/problems/spiral-matrix-ii/discuss/22282/4-9-lines-Python-solutions
    def generateMatrix(self, n):
        A, lo = [[n*n]], n*n
        while lo > 1:
            lo, hi = lo - len(A), lo
            A = [list(range(lo, hi))] + list(zip(*A[::-1])) # rotate clockwise
        return A

class Solution_right_turn: # https://leetcode.com/problems/spiral-matrix-ii/discuss/22282/4-9-lines-Python-solutions
    def generateMatrix(self, n):
        A = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for k in range(n*n):
            A[i][j] = k + 1
            if A[(i+di)%n][(j+dj)%n]:
                di, dj = dj, -di
            i += di
            j += dj
        return A

class Solution_neater_same_time:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0 for i in range(n)] for i in range(n)]
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        current_direction = 0
        x = y = 0
        for i in range(1, n * n + 1):
            mat[x][y] = i
            dx, dy = direction[current_direction]
            if(x + dx < 0 or x + dx > n - 1 or y + dy < 0 or y + dy > n - 1 or mat[x + dx][y + dy] != 0):
                current_direction = (current_direction + 1) % 4
            x += direction[current_direction][0]
            y += direction[current_direction][1]
        return mat

# recursive, Java solution
# class Solution {
#     public int[][] generateMatrix(int n) {
        
#         int ans[][] = new int[n][n];
#         fillMatrix(ans, 0 , 0, 1,'r');
#         return ans;
#     }
    
#     public void fillMatrix(int [][]ans, int i, int j, int cur, char dir){
#         if(i < 0 || j < 0 || i >=ans.length ||  j >= ans.length) return;
        
#         if(ans[i][j] != 0) return;
        
#         ans[i][j] = cur;
        
#         if(dir == 'u'){
#             fillMatrix(ans, i-1,j,cur+1, 'u');    
#         }
        
#         fillMatrix(ans, i,j+1,cur+1, 'r');
#         fillMatrix(ans, i+1,j,cur+1, 'd');
#         fillMatrix(ans, i,j-1,cur+1, 'l');
#         fillMatrix(ans, i-1,j,cur+1, 'u');
       
#     }
# }

class Solution_fastest:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0 for _ in range(n)] for _ in range(n)]
        rowStart = 0
        colStart = 0
        colEnd = n-1
        rowEnd = n-1
        num = 1
        while(rowStart<=rowEnd and colStart<=colEnd):            
            for i in range(colStart,colEnd+1):
                ans[rowStart][i]=num
                num+=1
            rowStart += 1
                
            for j in range(rowStart,rowEnd+1):
                ans[j][colEnd]=num
                num+=1
            colEnd -=1

            for k in range(colEnd,colStart-1,-1):
                ans[rowEnd][k]=num
                num+=1
            rowEnd -=1
            
            for l in range(rowEnd,rowStart-1,-1):
                ans[l][colStart]=num
                num+=1
            colStart +=1
        
        return ans