class Solution_mine_BFS:
    # time O(n^2); depth of BFS at most 4 by four-square theorem, O(N^0.5) ** 4 = O(N^2)
    # every natural number can be represented by the sum of four square integers
    # space O(n^2) too BFS has the same space and time complexity upper bound
    # quite slow, 1428 ms, but beats 65% though
    def numSquares(self, n: int) -> int:
        if n == (math.isqrt(n) ** 2):
            return 1
        squares = [(n ** 2, 1) for n in range(1, int(math.sqrt(n)) + 1)] # (square, distance)
        stack = deque(squares)
        visited = set(squares)
        while stack:
            now, dist = stack.popleft()
            # print(now, dist)
            if now == n:
                return dist
            for (square, _) in squares:
                new = now + square
                if new <= n and new not in visited:
                    visited.add(new)
                    stack.append((new, dist +1))
                    
# There are so many "large" test cases that it's worthwhile to keep data between test cases 
# rather than recomputing from scratch all the time. At least in the slower languages. 
# My dp tells the numbers of squares needed for the first integers, 
# and when asked about a new n, I extend dp just as much as necessary.

# https://leetcode.com/problems/perfect-squares/discuss/71512/Static-DP-C%2B%2B-12-ms-Python-172-ms-Ruby-384-ms
class Solution_static_DP:
    _dp = [0]
    def numSquares(self, n):
        dp = self._dp
        while len(dp) <= n:
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]

# from functools import lru_cache
class Solution_BFS_faster:
    # @lru_cache(None) # not recommended, using visited = set() is much better
    # 160 ms, beats 92%
    def numSquares(self, n):
        if n < 2:
            return n
        lst, visited = [], set()
        i = 1
        while i * i <= n:
            lst.append( i * i )
            i += 1
        cnt = 0
        toCheck = {n}
        while toCheck:
            cnt += 1
            temp = set()
            for x in toCheck:
                for y in lst:
                    if x == y:
                        return cnt
                    if x < y:
                        break
                    if x-y not in visited:
                        temp.add(x-y)
                        visited.add(x-y)
            toCheck = temp
        return cnt

# https://leetcode.com/problems/perfect-squares/discuss/707517/Python-no-DP-O(N)
class Solution_math:
    # you don't need more than 4 summands (Lagrange's four-square theorem)
    # also see three-square theorem https://en.wikipedia.org/wiki/Legendre%27s_three-square_theorem
    def numSquares(self, n: int) -> int:
        arr, i = [], 1
        while i**2 <= n:
            arr.append(i**2)
            i += 1
        
        #one-sum O(N^(1/2))
        if n in arr:
            return 1
        
        #two-sum O(N)
        for e in arr:
            if n-e in arr:
                return 2
        
        #three-sum O(N)
        arr_set = set(arr)
        for i in range(len(arr)):
            for j in range(len(arr)):
                if n-arr[i]-arr[j] in arr_set:
                    return 3
        
        #four-sum O(1)
        return 4