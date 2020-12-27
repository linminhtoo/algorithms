# https://leetcode.com/problems/decode-ways/submissions/
# https://leetcode.com/problems/decode-ways/discuss/253018/Python%3A-Easy-to-understand-explanation-bottom-up-dynamic-programming
class Solution_dp_table:
    def numDecodings(self, s: str) -> int:
        if not s or s[0]=='0':
            return 0

        dp = [0 for x in range(len(s) + 1)] 

        # base case initialization
        dp[0:2] = [1,1]

        for i in range(2, len(s) + 1): 
            # One step jump
            # need to ignore if it is '0', since it must belong to '10' or '20' which is handled below
            if 0 < int(s[i-1:i]):    #(2)  
                dp[i] = dp[i - 1]
            # Two step jump
            if 10 <= int(s[i-2:i]) <= 26: #(3)
                dp[i] += dp[i - 2]
                
        return dp[-1]

def memoize(f):
    memo = {}
    def wrapper(*args):
        if args not in memo:
            memo[args] = f(*args)
        return memo[args]
    return wrapper
# what are we memoizing? note that self.numDecodings(s[:-1]) will evaluate first. 
# as this recursive stack finishes, we already traversed the string s once
# so when we evaluate self.numDecodings(s[:-2]), we can make use of some of the results we already calculated
# this uses up more memory than the approach on top
class Solution_memoize:
    @memoize
    def numDecodings(self, s):
        if len(s) == 0:
            return 1
        elif len(s) == 1:
            if s[0] == '0':
                return 0
            else:
                return 1
        if int(s[-1]) > 0:
            if 9 < int(s[-2:]) < 27:
                return self.numDecodings(s[:-1]) + self.numDecodings(s[:-2])
            else:
                return self.numDecodings(s[:-1])
        elif 9 < int(s[-2:]) < 27:
            return self.numDecodings(s[:-2])
        else:
            return 0