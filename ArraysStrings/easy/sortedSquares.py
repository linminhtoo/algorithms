import collections
# https://leetcode.com/problems/squares-of-a-sorted-array/discuss/222079/Python-O(N)-10-lines-two-solutions-explained-beats-100
class Solution_two_pointers_fastest:
    def sortedSquares(self, A):
        answer = collections.deque()
        l, r = 0, len(A) - 1
        while l <= r: 
            # the trick is that if l == r, we go into 'else' and appendleft right**2
            left, right = abs(A[l]), abs(A[r])
            if left > right:
                answer.appendleft(left * left)
                l += 1
            else:
                answer.appendleft(right * right)
                r -= 1
        return list(answer)

class Solution_two_pointers_nodeque:
    def sortedSquares(self, A):
        l, r, answer = 0, len(A) - 1, [0] * len(A)
        while l <= r:
            left, right = abs(A[l]), abs(A[r])
            answer[r - l] = max(left, right) ** 2
            l, r = l + (left > right), r - (left <= right)
        return answer

class Solution_mine_two_pointers_not_so_fast:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0 # for positive numbers
        while i <= len(nums) - 1:
            if nums[i] >= 0:
                break
            i += 1
            
        nums = [i**2 for i in nums]
        if i == 0: # arr has non-negative numbers only
            return nums
        
        out = []
        j = i - 1 # for negative numbers, count backwards
        while i <= len(nums) - 1 and j >= 0:
            if nums[j] > nums[i]:
                out.append(nums[i])
                i += 1 # count forwards
            else:
                out.append(nums[j])
                j -= 1
        # clear remaining numbers in nums
        if i != len(nums):
            for idx in range(i, len(nums), 1):
                out.append(nums[idx])
        elif j != -1:
            for idx in range(j, -1, -1):
                out.append(nums[idx])
        return out

class Solution_nobrainer: 
    # no algo knowledge needd. will pass bcos max length is 10**4
    # and bcos array is almost sorted, so worst case of sorting won't be that slow
    # anyway time complexity is O(NlogN) which is more than enough to pass even in worst case
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = [i ** 2 for i in nums]
        nums.sort()
        return nums