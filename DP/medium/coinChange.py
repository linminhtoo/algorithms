from collections import deque
class Solution:
    # BFS? should work i think
    # but how to tell if no valid combo exists
    # is it when all numbers are > target
    def coinChange(self, coins: List[int], amount: int) -> int:
        q = deque([(0, 0)])
        visited = set()
        while q:
            curr, dist = q.popleft()
            if curr == amount:
                return dist
            
            for coin in coins:
                new = curr + coin
                # if new > amount, bcos all coins[i] > 0, it is now impossible to get amount
                # therefore, dont bother checking this curr amount anymore & check next in queue
                if new <= amount and new not in visited:
                    visited.add(new)
                    q.append((new, dist + 1))
            
        return -1

class Solution_DP_topdown:
    def coinChange(self, coins, amount):
        def helper(coins, amount, memo):
            if amount == 0: return 0
            if amount < 0: return -1
            
            if amount in memo:
                return memo[amount]
            else:
                min_dist = float('+inf')
                for coin in coins:
                    if amount - coin >= 0:
                        res = 1 + helper(coins, amount - coin, memo)
                        if res >= 1:
                            min_dist = min(min_dist, res)
                if min_dist != float('+inf'):
                    memo[amount] = min_dist
                    return min_dist
                else:
                    # dont forget this line!!! if not, will TLE
                    memo[amount] = -1
                    return -1              
        return helper(coins, amount, {})
        
    
class Solution_DP_bottomup:
    def coinChange(self, coins, amount):
        dp = [0] + [float('inf')] * amount
        
        for coin in coins:
            for i in range(coin, amount+1):
                # i represents amount we want
                # i - coin is amount before we add coin, +1 bcos that's the cost
                dp[i] = min(dp[i], dp[i-coin]+1)
        
        return dp[-1] if dp[-1] != float('inf') else -1