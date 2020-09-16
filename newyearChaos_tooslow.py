# https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict 

# Bubble sort with defaultdict, is too slow :((( 
# did not pass test cases 6, 7, 8, 9
def minimumBribes(q):
    swaps = defaultdict(int)
    n = len(q) 
  
    # Traverse through all array elements 
    for i in range(n-1): 
    # range(n) also work but outer loop will repeat one time more than needed. 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if q[j] > q[j+1] : 
                q[j], q[j+1] = q[j+1], q[j] 
                swaps[q[j+1]] += 1
                if swaps[q[j+1]] > 2:
                    print('Too chaotic')
                    return
    print(sum(swaps.values()))

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
