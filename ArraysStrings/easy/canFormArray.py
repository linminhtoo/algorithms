from typing import List
# https://leetcode.com/explore/featured/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3589/
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        found_js = set()
        master_i = 0
        while master_i <= len(arr) - 1: # check arr ele by ele
            # print(master_i, found_js)
            j = 0
            found = False # have we found a piece that matches current ele in arr? (master_i)
            while j <= len(pieces) - 1: # always start from 0, skipping found_js
                if found:
                    break
                if j in found_js:
                    j += 1
                    continue
                else:
                    k = 0
                    temp_i = master_i
                    while k <= len(pieces[j]) - 1:
                        # print(f'temp_i: {temp_i}, master_i: {master_i}, j: {j}, k: {k}, found: {found}')
                        if arr[temp_i] == pieces[j][k]:
                            k += 1
                            temp_i += 1
                            if k == len(pieces[j]): # traversed the whole of current piece at idx j
                                master_i = temp_i
                                found_js.add(j)
                                found = True
                                # k loop will exit since k > len(pieces[j]) - 1
                        else: # not matching elements and have not traversed whole of current piece
                            # move onto next piece by incrementing j
                            j += 1 # k = 0
                            break
            if not found:
                return False
            if len(found_js) == len(pieces):
                return True
        if len(found_js) == len(pieces):
                return True
                
class Solution_concise: # https://leetcode.com/problems/check-array-formation-through-concatenation/discuss/918408/Python-5-lines-hashmap
    # use first ele of each piece as key in hashmap
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        mp = {x[0]: x for x in pieces}
        res = []
        
        for num in arr:
            res += mp.get(num, [])
            
        return res == arr