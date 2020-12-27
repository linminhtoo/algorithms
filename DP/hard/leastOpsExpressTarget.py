# https://leetcode.com/problems/least-operators-to-express-number/discuss/208445/c%2B%2B-recursive-easy-to-understand
from functools import lru_cache
class Solution_dp_memoization: # top down, recursive
    @lru_cache(maxsize=None)
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        if x > target:
            return min(target * 2 - 1, (x - target) * 2)
        if x == target:
            return 0
        times = 0
        total = x
        while total < target:
            total *= x
            times += 1
        subtract = float("inf")
        if total - target < target:
            subtract = self.leastOpsExpressTarget(x, total - target) + times
        add = self.leastOpsExpressTarget(x, target - (total // x)) + times - 1
        return min(add, subtract) + 1 # add 1 bcos 1 extra operation is added (i.e. 1 level deeper in recursive stack)

# not the fastest but passes. good enough
# int leastOpsExpressTarget(int x, int target) {
# 		// At this time, you can get target either by add target times x/x or subtract (x - target) times x/x to x
# 		// For example, x = 3, target = 2. Then, 3/3 + 3/3 or 3 - 3/3 is possible result
#         if (x > target) {
#             return min(target * 2 - 1, (x - target) * 2);
#         }
#         if (x == target) {  // just push x at the end
#             return 0;
#         }
        
#         long long sums = x;
#         int times = 0;
#         while (sums < target) {  // this is gready, put as much as possible 'x'
#             times++;
#             sums *= x;
#         }
        
#         if (sums == target) {  // one more 'x' you put, one more operator
#             return times;
#         }
        
# 		// when you have remainder, you have two choices, one is add, the other is subtract
# 		// for example, x = 3, target = 5. Then, 5 = 3 + 2 or 5 = 9 - 4
#         int l = INT_MAX, r = INT_MAX;
#         if (sums - target < target) {
#             l = leastOpsExpressTarget(x, sums - target) + times;  // using subtract
#         }
#         r = leastOpsExpressTarget(x, target - (sums / x)) + times - 1;  // using add
#         return min(l, r) + 1;  // No matter +/- used, one more operator is add
#     }

# improvement using dfs+memoization
#  unordered_map<int, int> memo;
#     int leastOpsExpressTarget(int x, int target) {
#         return dfs(x, target);
#     }
#     int dfs(int x, int target){
#         if(memo.count(target)) return memo[target];
#         if(target < x)
#             return min(target*2-1, (x - target)*2);
#         else if( target == x) return 0;
#         long sigma = x, mcnt = 0;
#         while(sigma < target){
#             sigma*=x;
#             mcnt++;
#         }
#         if(sigma == target) return memo[target] = mcnt;
#         memo[target] = INT_MAX;
#         if(sigma - target < target)
#             memo[target] = dfs(x, sigma - target) + mcnt + 1;
#         return memo[target] = min((long)memo[target], dfs(x, target - sigma/x) + mcnt);
#     }