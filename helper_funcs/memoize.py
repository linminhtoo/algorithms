def memoize(f):
    memo = {}
    def wrapper(*args):
        if args not in memo:
            memo[args] = f(*args)
        return memo[args]
    return wrapper

# see DP --> medium --> numDecodings for details
# https://leetcode.com/problems/decode-ways/submissions/