from typing import List
class Solution_mine: # pass, O(N), but maybe not concise?
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        i = 0
        increasing_count = 0
        increasing = True
        while i + 1 <= len(arr) - 1:
            if increasing:
                if arr[i] == arr[i+1]:
                    return False
                elif arr[i] > arr[i+1]:
                    increasing = False
                else:
                    increasing_count += 1
            if not increasing:
                if arr[i] <= arr[i+1]:
                    return False
            i += 1
        return not increasing and increasing_count >= 1