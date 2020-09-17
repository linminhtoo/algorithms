# https://leetcode.com/problems/image-overlap/discuss/138976/A-generic-and-easy-to-understand-method
# https://leetcode.com/problems/design-hashmap/discuss/185347/Hash-with-Chaining-Python

from Typing import List

class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        num_row, num_col = len(A), len(A[0])
        la, lb = [], []
        for row in range(num_row):
            for col in range(num_col):
                if A[row][col] == 1:
                    la.append([row, col])
                if B[row][col] == 1:
                    lb.append([row,col])
        
        store = dict()
        
        for pa in la:
            for pb in lb:
                translation_vector = (pb[0] - pa[0], pb[1] - pa[1])
                if translation_vector not in store:
                    store[translation_vector] = 0
                store[translation_vector] += 1
        
        if not store.values():
            return 0
        
        return max(store.values())