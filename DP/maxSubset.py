# https://www.hackerrank.com/challenges/max-array-sum/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=dynamic-programming
#!/bin/python3

import math
import os
import random
import re
import sys

# DYNAMIC PROGRAMMING
# tried to save space complexity but could not do it, keep getting weird bug
# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    max_at_each_pos = [0] * len(arr)
    max_at_each_pos[0] = arr[0]
    max_at_each_pos[1] = max(arr[0], arr[1])
    i = 2
    while i < len(arr):
        max_thus_far = max(arr[i], max_at_each_pos[i-2] + arr[i], max_at_each_pos[i-1])
        max_at_each_pos[i] = max_thus_far
        i += 1

    return max(max_at_each_pos)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
