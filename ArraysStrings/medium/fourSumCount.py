from typing import List
from collections import Counter, defaultdict
# https://leetcode.com/problems/4sum-ii/discuss/93917/Easy-2-lines-O(N2)-Python
class Solution_pass: # break down O(N^3) into O(2N^2) is much faster
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        AB, CD = defaultdict(int), defaultdict(int)
        for i in range(len(A)):
            for j in range(len(B)):
                AB[A[i] + B[j]] += 1
        
        for k in range(len(C)):
            for l in range(len(D)):
                CD[C[k] + D[l]] += 1
        
        total = 0
        for ab in AB:
            total += CD[-ab] * AB[ab]
        return total

class Solution_concise: # also O(N^2), just more concise
    def fourSumCount(self, A, B, C, D):
        AB = collections.Counter(a+b for a in A for b in B)
        return sum(AB[-c-d] for c in C for d in D)

class Solution_tooslow: # O(N^3), not expected to pass. fails last few test cases
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        D_count = Counter(D)
        total = 0
        for i in range(len(A)):
            for j in range(len(B)):
                for k in range(len(C)):
                    cur_sum = A[i] + B[j] + C[k]
                    to_find = 0 - cur_sum
                    if to_find in D_count.keys():
                        total += D_count[to_find]
        
        return total