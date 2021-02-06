# https://leetcode.com/problems/longest-palindromic-subsequence/submissions/
# very similar to longest common subsequence
# NOTE: when memoizing, make sure only l & r are parameters. do not have other params like
# count, as these can cause problems. also rmbr base cases do not need to be memoized
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = [[0 for _ in range(len(s))] for _ in range(len(s))]
        def helper(s, l, r, memo):
            if l > r:
                return 0
            elif l == r:
                return 1
                    
            if memo[l][r] > 0:
                return memo[l][r]
            else:
                if s[l] == s[r]:
                    memo[l][r] = 2 + helper(s, l+1, r-1, memo)
                else:
                    memo[l][r] = max(
                            helper(s, l+1, r, memo),
                            helper(s, l, r-1, memo)
                        )
                return memo[l][r]

        return helper(s, 0, len(s)-1, memo)
    
    def longestPalindromeSubseq_O2expN_(self, s: str) -> int:
        def helper(s, l, r):
            if l > r:
                return 0
            elif l == r:
                return 1
            elif s[l] == s[r]:
                return 2 + helper(s, l+1, r-1)
            else:
                return max(
                    helper(s, l+1, r),
                    helper(s, l, r-1)
                )
        
        return helper(s, 0, len(s)-1)
    
    def longestPalindromeSubseq_O2expN(self, s: str) -> int:
        count = 0
        def helper(s, count):
            if s == '':
                return count
            elif s[0] == s[-1]:
                return helper(s[1:-1], count + 2)
            else:
                return max(
                    helper(s[1:], count),
                    helper(s[:-1], count)
                )
        
        return helper(s, count)