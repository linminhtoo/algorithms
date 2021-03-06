# https://leetcode.com/problems/longest-palindromic-substring/submissions/

# nice DP solution
# https://leetcode.com/problems/longest-palindromic-substring/discuss/151144/Bottom-up-DP-Logical-Thinking

class Solution: # mine but not the fastest, since I have to loop twice. time O(N^2)
    def longestPalindrome(self, S: str) -> str:
        best = (0, 0)
        longest = 1
        for i in range(len(S)):
            l, r = i, i + 1
            length = 0
            while l >= 0 and r <= len(S) - 1 and S[l] == S[r]:
                l -= 1
                r += 1
                length += 2
            if length > longest:
                best = (l+1, r-1)
                longest = length
                
        for i in range(len(S)):
            l, r = i - 1, i + 1
            length = 1
            while l >= 0 and r <= len(S) - 1 and S[l] == S[r]:
                l -= 1
                r += 1
                length += 2
            if length > longest:
                best = (l+1, r-1)
                longest = length
        
        best_l, best_r = best
        return S[best_l:best_r+1]

class Solution_dp: # dp solution from link above, but actually it is quite slow, 8556 ms O(N^2)
    def longestPalindrome(self, S: str) -> str:
        dp = [[False for _ in range(len(S))] for _ in range(len(S))]
        for i in range(len(S)):
            dp[i][i] = True
        
        longest, start = 1, 0
        for i in range(len(S) - 1, -1, -1):
            for j in range(i + 1, len(S)):
                if S[i] == S[j]:
                    if j - i == 1 or dp[i+1][j-1]:
                        dp[i][j] = True
                        if j - i + 1 > longest:
                            longest = j - i + 1
                            start = i
        # print(dp)
        # print(start, longest)
        return S[start:start+longest]

class Solution_nodptable:
    # @return a string
    def longestPalindrome(self, s):
        if len(s)==0:
        	return 0
        maxLen=1
        start=0
        for i in range(len(s)):
            # move pointer left by 1
        	if i-maxLen >=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:
        		start=i-maxLen-1
        		maxLen+=2
        		continue

            # do not move pointer left
        	if i-maxLen >=0 and s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:
        		start=i-maxLen
        		maxLen+=1
        return s[start:start+maxLen]