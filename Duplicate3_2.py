import logging
from typing import List
from collections import deque 

class Solution:
    @staticmethod
    def containsNearbyAlmostDuplicate(nums: List[int], k: int, t: int) -> bool:
        left, right = 0, k
        right = min(len(nums) - 1, right)
        while right < len(nums):
            window = sorted(nums[left : right + 1])
            window_minus = deque(window)
            window_minus.popleft()
            window_minus.append(-2e31-1)
            window_minus = list(window_minus)
            difference = [window[i] - window_minus[i] for i in range(len(window))]
            print(difference)
            result = list(filter(lambda x: 1 if x < t else 0, difference))
            print(result)
            if sum(result) > 0:
                return True
            left += 1
            right += 1
        return False

if __name__ == '__main__':
    print(Solution.containsNearbyAlmostDuplicate([1, 0, -1, 4], k=2, t=1))
    