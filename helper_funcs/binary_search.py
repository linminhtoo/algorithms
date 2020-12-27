from typing import List

# https://docs.python.org/3/library/bisect.html
from bisect import bisect_left
class Solution_python_builtin:
    def binary_search(self, element: int, A: List[int]) -> int: 
        A.sort()
        idx = bisect_left(A, element)
        if idx != len(A) and A[idx] == element:
            return idx
        else:
            return -1 # not found

# https://stackabuse.com/binary-search-in-python/
class Solution_recursive:
    def binary_search(self, element: int, A: List[int]) -> int: 
        A.sort()
        def helper(a: int, nums: List[int], start: int, end: int) -> List[int]:
            if start > end:
                return -1
            mid = (start + end) // 2
            if a == nums[mid]:
                return mid
            if a < nums[mid]:
                return helper(a, nums, start, mid-1)
            else:
                return helper(a, nums, mid+1, end)
        return helper(element, A, 0, len(A)) # not len(A) - 1

class Solution_iterative:
    def binary_search(self, element: int, A: List[int]) -> int: 
        A.sort()
        start, end = 0, len(A)
        while start <= end:
            mid = (start + end) // 2
            if element == A[mid]:
                return mid
            if element < A[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1 # not found
            
