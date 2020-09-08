# https://leetcode.com/problems/bulb-switcher-iv/
class Solution:
    def minFlips(self, target: str) -> int:
        counter = 0
        if target[0] == '1':
            counter += 1
        for idx in range(len(target) - 1):
            if target[idx] != target[idx+1]:
                counter += 1
        return counter

from functools import reduce
class Solution_reduce:
    def minFlips(self, target: str) -> int:
        return reduce(lambda x, y: (x[0] + (x[1] != y), y), target, (0, '0'))[0]

# 78.1% faster than others
# 96% less memory than others
print(Solution().minFlips('101110101'))
print(Solution_reduce().minFlips(('101110101')))
# 7