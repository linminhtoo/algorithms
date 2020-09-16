# https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
# GETTING THE WRONG ANSWER!!! too many swaps 
def qs(arr, left, right):
    if left >= right:
        return 0

    pivot, now_swaps = partition(arr, left, right)
    left_swaps = qs(arr, left, pivot - 1)
    right_swaps = qs(arr, pivot + 1, right)
    # print(now_swaps, left_swaps, right_swaps)

    return now_swaps + left_swaps + right_swaps

def partition(arr, left, right):
    now_swaps = 0
    pivot = arr[right]

    i = left - 1
    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
            now_swaps += 1

    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1, now_swaps

def minimumSwaps(arr):
    return qs(arr, 0, len(arr) - 1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
