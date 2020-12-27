import math
class Solution_integer:
    def isPalindrome(self, x: int) -> bool:  
        if x < 0:
            return False
        
        if (x < 10 and x >= 0):
            return True
        # if x % 11 == 0: # doesn't work for 1122, which is divisible by 11 but is not a palindrome
        #     return True
        nums = [] 
        x_orig = x
        while len(nums) < math.floor(math.log10(x_orig)) + 1 and x > 0:
            q, r = divmod(x, 10)
            nums.append(r)
            x = q
            # print(q, r, x)
        # print(nums)
        i = 0
        j = len(nums) - 1
        while i < j: # loop through all digits of nums
            if nums[i] != nums[j]:
                return False
            i += 1
            j -= 1
        return True