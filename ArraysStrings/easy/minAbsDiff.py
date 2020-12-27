from typing import List
# https://leetcode.com/problems/minimum-absolute-difference/submissions/
class Solution_mine: # 400 ms
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        i = 0
        diffs, target = [], float('+inf')
        while i + 1 <= len(arr) - 1:
            diff = arr[i+1] - arr[i]
            diffs.append(diff)
            target = min(target, diff)
            i += 1
        out = []
        j = 0
        while j <= len(diffs) - 1:
            if diffs[j] == target:
                out.append((arr[j], arr[j+1]))
            j += 1
        return out

class Solution_3lines: 
    # conceptually it's exactly the same. note the nice use of ZIP (which also makes it faster)
    # 336 ms
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mn = min(b - a for a, b in zip(arr, arr[1:]))
        return [[a, b] for a, b in zip(arr, arr[1:]) if b - a == mn]        