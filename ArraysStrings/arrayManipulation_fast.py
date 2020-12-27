# https://www.hackerrank.com/challenges/crush/forum?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
class Solution_fast:
    def arrayManipulation(self, n, queries):
        array = [0] * (n + 1)
        
        for query in queries: 
            a = query[0] - 1
            b = query[1]
            k = query[2]
            array[a] += k
            array[b] -= k
            
        max_value = 0
        running_count = 0
        for i in array:
            running_count += i
            if running_count > max_value:
                max_value = running_count
                
        return max_value

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the arrayManipulation function below.
# KEEP GETTING RUNTIME ERROR on test cases 7 to 13 
def arrayManipulation(n, queries):
    mapping = {i: 0 for i in range(1, n+1)}
    for q in queries:
        for one_index in range(q[0], q[1]+1):
            mapping[one_index] += q[2]
    
    return max(mapping.values())


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    s = Solution_fast
    result = s.arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()