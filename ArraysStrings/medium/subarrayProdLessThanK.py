from typing import List
class Solution_two_pointer_mine: # or sliding window
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        a, b = 0, 0
        prod = 1
        total = 0
        while b <= len(nums) - 1:
            prod *= nums[b]
            while prod >= k and a <= len(nums) - 1:
                prod /= nums[a]
                a += 1
            total += max(b - a + 1, 0)
            b += 1
        return total

class Solution_log: # but not very intuitive to me
    def numSubarrayProductLessThanK(self, nums, k):
        if k == 0: return 0
        k = math.log(k)

        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + math.log(x))

        ans = 0
        for i, x in enumerate(prefix):
            j = bisect.bisect(prefix, x + k - 1e-9, i+1)
            ans += j - i - 1
        return ans