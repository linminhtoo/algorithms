from collections import defaultdict, OrderedDict

# from codility, called MissingIntegers
def solution(A):
    # write your code in Python 3.6
    if not A:
        return 1
        
    i = 0
    counter = defaultdict(int)
    while i <= len(A) - 1:
        if A[i] <= 0:
            i += 1
        else:
            counter[A[i]] += 1
            i += 1
    
    counter = OrderedDict(sorted(counter.items()))
    # ordereddict preserves order of keys from sorting
    idx = 1
    for key, val in counter.items():
        if idx != key:
            return idx
        idx += 1
    return idx