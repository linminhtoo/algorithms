# https://leetcode.com/problems/coin-change-2/
# https://leetcode.com/problems/coin-change-2/discuss/675096/Python-O(amount-*-N)-simple-dp-explained-(updated)
from typing import List

class Solution_recursive_memo:
    # naive recursive will TLE for sure
    # key to memo is to use remaining_amount & coin_idx
    # unbounded knapsack problem (add current coin or skip and move on),
    # just that if we do add current coin, we STAY at current coin_idx (instead of moving on)
    def change(self, amount: int, coins: List[int]) -> int:
        L = len(coins)
        def helper(rem, coin_idx, memo):
            if rem == 0:
                return 1
            if rem < 0 or coin_idx >= L:
                return 0
            
            if memo[rem][coin_idx] is not None:
                return memo[rem][coin_idx]
            else:
                add = helper(rem - coins[coin_idx], coin_idx, memo)
                skip = helper(rem, coin_idx+1, memo)
                memo[rem][coin_idx] = add + skip
                return add + skip
        memo = [[None for _ in range(L)] for _ in range(amount+1)]
        return helper(amount, 0, memo)
        
from collections import deque
class Solution_BFS_alsoTLE:
    def change(self, amount: int, coins: List[int]) -> int:
        q = deque([(amount, [])])
        res = []
        seen = [] # not sure if having this is better or worse, but both TLE anyway
        while q:
            rem, path = q.popleft()
            if rem == 0:
                path.sort()
                if path not in res:
                    res.append(path)
                    
            else:
                for coin in coins:
                    if rem - coin >= 0:
                        path_ = path + [coin]
                        path_.sort()
                        if path_ not in seen:
                            seen.append(path_)
                            q.append((rem - coin, path + [coin]))
        return len(res)
        
class Solution_recursive_TLE:
    def change(self, amount: int, coins: List[int]) -> int:
        self.res = []
        def helper(rem, path):
            if rem == 0 and path not in self.res:
                self.res.append(path)
                return
            
            for coin in coins:
                if rem - coin >= 0:
                    path_ = path.copy()
                    path_[coin] += 1
                    helper(rem - coin, path_)
                    
        helper(amount, defaultdict(int))
        return len(self.res)