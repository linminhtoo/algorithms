from typing import List
# https://leetcode.com/problems/gas-station/submissions/
class Solution:
    # 2 ideas:
    # sum(gas) >= sum(cost) to have solution
    # otherwise, there will be at least one station where our tank < 0

    # if A cannot reach B, any station between A & B cannot reach B too,
    # provided B is the first such station A cannot reach
    # this can be proven by contradiction
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        start = 0
        tank = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1 # none of those stations so far can be a solution
                tank = 0 # reset tank
        return start