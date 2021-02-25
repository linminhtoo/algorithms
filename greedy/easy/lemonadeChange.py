# https://leetcode.com/problems/lemonade-change/submissions/
from collections import defaultdict
from typing import List
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cash = defaultdict(int)
        
        for b in bills:
            if b == 10:
                if cash[5] == 0:
                    return False
                cash[5] -= 1
            elif b == 20:
                # it is critical to give 10 as change first whenever possible
                if cash[10] > 0 and cash[5] > 0:
                    cash[10] -= 1
                    cash[5] -= 1
                elif cash[5] > 2:
                    cash[5] -= 3
                else:
                    return False
            cash[b] += 1
            # print(b, cash)
        
        return True