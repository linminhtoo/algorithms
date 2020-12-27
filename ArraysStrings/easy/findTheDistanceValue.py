from typing import List
class Solution_naive:
    # passes, but not very fast, 104ms
    def findTheDistanceValue(self, A: List[int], B: List[int], d: int) -> int:
        count = 0
        for a in A:
            valid = True
            for b in B:
                if abs(b - a) <= d:
                    valid = False
                    break
            if valid:
                count += 1
        return count

from bisect import bisect_left
class Solution_binary_search_mine: 
    # beats 96% time, 72ms
    def findTheDistanceValue(self, A: List[int], B: List[int], d: int) -> int:
        B.sort()
        count = 0
        for a in A:
            i = bisect_left(B, a)
            if i == len(B):
                valid = not (abs(B[i-1] - a) <= d) # not (True) evaluates to False
            elif i == 0:
                valid = not (abs(B[i] - a) <= d) 
            else:
                valid = not (abs(B[i-1] - a) <= d or abs(B[i] - a) <= d)
            count += (valid) # (True) evaluates to 1, (False) evaluates to 0
        return count

# Some remarks on how to interpret this algorithm.
#
# Each branch of the nested if-else statement will lead you to a single conclusion about your
# current configuration of pointers regarding two questions:
# 1. does the i-th element of arr1 sastisfies distance condition or not -- if not we drop i-th
# element, i.e. ignore augmenting distance counter and advance the pointer
# 2. is the j-th element of arr2 neccessary for comparisons with current or next elements of
# arr1 -- if not we advance the j pointer
#
# The concluding correction accounts for the tail of arr1 in the case when its values are greater
# than all of the arr2. I need it because my algorithm for the sake of simplicity and its
# correctness assumes that there will be always a concluding element of arr2 that is greater
# that any elmeent of arr1. You can see on the test sets it is not always the case, therefore is
# the correction.
class Solution_two_pointer: # interesting approach
    def findTheDistanceValue(self, arr1, arr2, d):
        arr1.sort()
        arr2.sort()
        i = 0
        j = 0
        dist = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] >= arr2[j]:
                if arr1[i] - arr2[j] > d:
                    j += 1
                else:
                    i += 1
            else:
                if arr2[j] - arr1[i] > d:
                    i += 1
                    dist += 1
                else:
                    i += 1
        dist += len(arr1) - i
        return dist