# https://leetcode.com/problems/prime-arrangements/discuss/371862/JavaPython-3-two-codes-each-count-only-primes-then-compute-factorials-for-both-w-analysis.
class Solution_divide_factors:    
    def numPrimeArrangements(self, n: int) -> int:
        cnt = 1                                                     # number of primes, first prime is 2.
        for i in range(3, n + 1, 2):                                # only odd number could be a prime, if i > 2.
            factor = 3
            while factor * factor <= i:
                if i % factor == 0:
                    break 
                factor += 2    
            else:
                cnt += 1        
        ans = 1
        for i in range(1, cnt + 1):                                # (number of primes)!
            ans *= i        
        for i in range(1, n - cnt + 1):                            # (number of non-primes)!
            ans *= i
        return ans % (10**9 + 7)
        # using math library we can replace last 6 lines above
        # return math.factorial(cnt) * math.factorial(n - cnt) % (10**9 + 7) 

# also from
# https://leetcode.com/problems/prime-arrangements/discuss/371862/JavaPython-3-two-codes-each-count-only-primes-then-compute-factorials-for-both-w-analysis.
# https://en.m.wikipedia.org/wiki/Sieve_of_Eratosthenes
class Solution_sieve_of_eratosthenes_mark_composites:
    def numPrimeArrangements(self, n: int) -> int:
        primes = [True] * (n + 1)
        for prime in range(2, int(math.sqrt(n)) + 1):
            if primes[prime]:
                for composite in range(prime * prime, n + 1, prime):
                    primes[composite] = False
        cnt = sum(primes[2:]) # 0 and 1 are not primes
        return math.factorial(cnt) * math.factorial(n - cnt) % (10**9 + 7)