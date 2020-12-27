# random mathy functions
def isPalindrome(s: str) -> bool:
    return s == s[::-1]

import math
def isPerfectSquare(n: int) -> bool:
    return math.isqrt(n) ** 2 == n