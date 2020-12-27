from typing import List
# interesting
# https://leetcode.com/problems/increasing-triplet-subsequence/discuss/78997/Generalization-in-Python

# https://leetcode.com/problems/increasing-triplet-subsequence/discuss/976393/Python-O(n)-solution-explained
# heuristic, easiest to understand
class Solution_correct_but_slow: # 9608 ms & 15.4 MB
    def increasingTriplet(self, nums: List[int]) -> bool:
        candidates = [[nums[0]]]
        seen = set() 
        i = 1 
        while i <= len(nums) - 1:
            added = False
            for j in range(len(candidates)):
                cand = candidates[j]
                if nums[i] > cand[-1]:
                    if len(cand) == 1 and frozenset([cand[-1], nums[i]]) not in seen:
                        cand.append(nums[i])
                        seen.add(frozenset(cand))
                        added = True
                    elif len(cand) == 2:
                        return True
                elif len(cand) == 2:
                    if nums[i] > cand[-2] and frozenset([cand[-2], nums[i]]) not in seen:
                        candidates.append([cand[-2], nums[i]])
                        seen.add(frozenset([cand[-2], nums[i]]))
                        added = True
            
            if not added and frozenset([nums[i]]) not in seen:
                candidates.append([nums[i]])
                    
            i += 1
            # print(candidates)
        return False

class Solution_veryfast:
    def increasingTriplet(self, nums):
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False

# if __name__ == '__main__':
#     Solution.increasingTriplet([1,6,2,5,1])