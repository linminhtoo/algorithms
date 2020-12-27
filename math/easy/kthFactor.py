# https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3554/

# https://leetcode.com/problems/the-kth-factor-of-n/discuss/959372/7-line-Java-O(sqrt-n)-time-O(1)-space-not-a-typical-explanation
# best is O(sqrt(N))
import math 
class Solution: 
    def kthFactor(self, n: int, k: int) -> int:
        root = math.sqrt(n)
        i = 1
        while i < root: # to avoid double counting sqrt
            if n % i == 0: 
                k -= 1
            if k == 0: 
                return i
            i += 1
        for j in range(int(root), 0, -1):
            if n % (n//j) == 0: # need to use // to divide n by j
                k -= 1
            if k == 0: 
                return n//j
        return -1       

# for(int i = 1; i < Math.sqrt(n); ++i) 
# 	if(n % i== 0 && --k == 0) 
# 		return i;                       
# for(int i = (int) Math.sqrt(n); i >= 1; --i) 
# 	if(n % (n/i) == 0 && --k == 0) 
# 		return n/i;          
# return -1;

class Solution_mine: # O(N)
    # optimize: stop once k == 0 (do k -= 1 for each factor found)
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        for i in range(1, n+1, 1):
            if n % i == 0: factors.append(i)
        if k - 1 <= len(factors) - 1:
            return factors[k-1]
        else:
            return -1