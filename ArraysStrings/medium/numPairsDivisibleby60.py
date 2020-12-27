from collections import Counter
from typing import List
class Solution_fast_mine: # v fast, O(N)
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        time = [t % 60 for t in time]
        
        counter = Counter(time)
        total = 0
        keys = list(counter.keys())
        for t in keys:
            if t == 0 or t == 30:
                to_add = counter[t] * (counter[t] - 1) / 2
            else:
                to_add = counter[t] * counter[60-t]
            total += to_add
            if to_add > 0:
                del counter[t], counter[60-t]
        
        return int(total)

class Solution_concise_2: # official solution
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainders = collections.defaultdict(int)
        ret = 0
        for t in time:
            if t % 60 == 0: # check if a%60==0 && b%60==0
                ret += remainders[0]
            else: # check if a%60+b%60==60
                ret += remainders[60-t%60]
            remainders[t % 60] += 1 # remember to update the remainders
        return ret

# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/discuss/256738/JavaC%2B%2BPython-Two-Sum-with-K-60
class Solution_concise:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ans = 0
        c = [0] * 61
        for x in time:
            m = x % 60
            ans += c[60 - m]
            c[m if m else 60] += 1 # if m == 0, check 60 
        return ans

class Solution_bruteforce_fail: # O(N^2), fails for last few test cases where N ~= 10**4 
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        time.sort()
        
        count = 0
        i = 0
        while i + 1 <= len(time) - 1:
            j = i + 1
            while j <= len(time) - 1:
                if (time[i] + time[j]) % 60 == 0:
                    count += 1
                j += 1
            i += 1
            
        return count