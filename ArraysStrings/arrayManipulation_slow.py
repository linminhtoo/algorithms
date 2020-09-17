#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the arrayManipulation function below.
# KEEP GETTING RUNTIME ERROR on test cases 7 to 13 (Pypy3 also fails LMAO)
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

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()





# from collections import defaultdict

# mydict = defaultdict(int)
# mydict[1] += 100
# mydict[2] += 200
# mydict[3] += 400

# print(max(mydict.values()))