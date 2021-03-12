from collections import Counter
# https://leetcode.com/problems/minimum-window-substring/
class Solution:
    # should be O(52N) = O(N)
    # but is quite slow, beats only 6%, maybe bcos 52 is high
    def minWindow(self, s: str, t: str) -> str:
        # related to max sliding window problem
        
        # naive bruteforce: starting from each index, find the minimum window
        # up to O(N^2) (need to check every index, and for each index, may need to check up to last char of s)
        # definitely TLE
        
        # realize that we are repeating a lot of work in the above approach
        # the difference between windows, is that we consider one less char on the left
        # if this left character was important to form t, then we may need to consider more char on the right
        # otherwise, we dont need to consider more char on the right
        
        # at idx 0, we may not find t even when end_idx == len(s) - 1, then we just return "" 
        # idx 0, ADOBEC
        # idx 1, DOBECODEBA
        # idx 2, OBECODEBA
        # idx 3, BECODEBA
        # idx 4, ECODEBA
        # idx 5, CODEBA
        # idx 6, ODEBANC
        # idx 7, DEBANC
        # idx 8, EBANC
        # idx 9, BANC --> our answer!
        # idx 10, cannot find new B on the right (no chars left), so stop
        
        # can use Counter to keep track of how many chars in t we have found so far
        # for a given start idx, we find minimum length when Counter(curr_substr) == Counter(t) for the first time
        # we need to track the smallest possible minimum length
        # we need two pointers: 2) start of curr_substr & 2) end of curr_substr
        t_cnt = Counter(t) # comparing two counters is at most O(26x2) time (lower & uppercase)
        l = 0
        r = 0
        min_len = float('+inf')
        l_min, r_min = 0, 0
        s_cnt = Counter()
        while l <= len(s) - 1:
            while t_cnt - s_cnt and r <= len(s) - 1:
                s_cnt[s[r]] += 1
                r += 1
            if not t_cnt - s_cnt:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    l_min, r_min = l, r
                l += 1
                s_cnt[s[l-1]] -= 1
            else:
                break
        return s[l_min:r_min]
            
        