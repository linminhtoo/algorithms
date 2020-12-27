# https://leetcode.com/problems/count-primes/submissions/
import math
class Solution: # sieve of Eratosthenes
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        
        primes = [True] * (n)
        for cand in range(2, int(math.sqrt(n)) + 1):
            if primes[cand]:
                for composite in range(cand * cand, n, cand):
                    primes[composite] = False
        return sum(primes[2:])