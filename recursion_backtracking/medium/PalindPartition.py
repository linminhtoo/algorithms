# https://leetcode.com/problems/palindrome-partitioning/discuss/41973/Python-recursiveiterative-backtracking-solution
# # possible partitions is O(2^N). considering a string of n same chars, like, 'aaaaaa...', 
# # possible partitions is the sum of (choose 0 from n-1), (1 from n-1), (n from n-1)... (n-1 from n-1) == 2^(n-1).
# Therefore.... the time complexity cannot be better than O(2^N)... 
# My guess is something like O(N*2^N), like checking each substring may take O(N) on average? Not sure though.
from typing import List
class Solution_dfs_backtracking:
    # 632 ms, 60% faster
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s: str, path: List[str], res: List[List[str]]) -> None:
        if not s:
            res.append(path)
            return
        for i in range(1, len(s)+1):
            if self.isPal(s[:i]):
                self.dfs(s[i:], path+[s[:i]], res)
        
    def isPal(self, s: str) -> bool:
        return s == s[::-1]

class Solution_dfs_backtracking_2: 
    # v similar to above, just uses self.res to store the results List[List[str]]
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def isPalindrome(start_ind, end_ind):
            while start_ind <= end_ind:
                if s[start_ind] != s[end_ind]: return False
                start_ind += 1
                end_ind -=1
            return True
        
        def dfs(start_ind, path):
            if start_ind >= len(s): self.res.append(path)
                
            for l in range(len(s) - start_ind):
                if isPalindrome(start_ind, start_ind + l):
                    dfs(start_ind + l + 1, path + [s[start_ind:start_ind + l + 1]] )
        
        self.res = []
        dfs(0,[])
        return self.res