from typing import List
# https://leetcode.com/problems/two-sum/discuss/?currentPage=1&orderBy=most_votes&query=
class Solution_twopass_hashmap:
    # exactly one valid solution always exists
    def twoSum(self, A: List[int], t: int) -> List[int]:
        hashmap = {a : i for i, a in enumerate(A)}
        for i, a in enumerate(A):
            if t - a in hashmap and hashmap[t - a] != i: # cannot use same index twice
                return [i, hashmap[t-a]]

class Solution_onepass_hashmap:
    # exactly one valid solution always exists
    def twoSum(self, A: List[int], t: int) -> List[int]:
        hashmap = {}
        for i, a in enumerate(A):
            if a in hashmap:
                return [hashmap[a], i]
            hashmap[t - a] = i