class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s: # empty string
            return 0
        # check if s is already palindrome
        left = 0
        right = len(s) - 1
        while left <= right: 
            if s[left] != s[right]:
                return 2 # s is not a palindrome
            left += 1
            right -= 1
        return 1 # s is a palindrome