# WRONG ANSWER! DK WHY 
# the counting moves part is wrong, need to debug

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict 

# Complete the minimumBribes function below.
def minimumBribes(q):
    def merge_defaultdicts(d,d1):
        for k, v in d1.items():
            d[k] += v
        return d
        
    def merge_sort_with_count(arr, left, right, swap_dict):
        if left >= right:
            return (0, arr[left: right+1], swap_dict)
        
        # if left == right - 1:
        #     if arr[left] > arr[right]:
        #         swap_dict[arr[left]] += 1 
        #         if swap_dict[arr[left]] > 2:
        #             print('Too chaotic')
        #             return None, None, None
        #         return (1, [arr[right], arr[left]], swap_dict)
        #     else:
        #         return (0, arr[left:right+1], swap_dict)

        middle = (left + right)//2
        
        ltotal, lSorted, lswaps = merge_sort_with_count(arr, left, middle, swap_dict)
        if ltotal is None:
            return None, None, None
        rtotal, rSorted, rswaps = merge_sort_with_count(arr, middle+1, right, swap_dict)

        if ltotal is None or rtotal is None:
            return None, None, None

        mswaps = merge_defaultdicts(lswaps, rswaps)
        mtotal = 0
        Sorted = []
        left_pointer = 0
        right_pointer = 0
        while left_pointer < len(lSorted) and right_pointer < len(rSorted):
            if lSorted[left_pointer] <= rSorted[right_pointer]:
                Sorted.append(lSorted[left_pointer])
                left_pointer += 1
            else:
                # mswaps[rSorted[right_pointer]] += 1
                # if mswaps[rSorted[right_pointer]] > 2:
                mswaps[lSorted[left_pointer]] += len(lSorted) - left_pointer
                if mswaps[lSorted[left_pointer]] > 2:
                    print('Too chaotic')
                    return None, None, None
                Sorted.append(rSorted[right_pointer])
                right_pointer += 1
                mtotal += len(lSorted) - left_pointer
        
        Sorted += lSorted[left_pointer:]
        Sorted += rSorted[right_pointer:]
            
        total = ltotal + rtotal + mtotal
        return total, Sorted, mswaps

    total, Sorted, mswaps = merge_sort_with_count(q, 0, len(q) - 1, defaultdict(int))
    if total is not None:
        print(total)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
