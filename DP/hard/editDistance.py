# https://leetcode.com/problems/edit-distance/discuss/159295/Python-solutions-and-intuition
class Solution:
    # TC is O(len(word1) * len(word2))
    # SC is identical
    def minDistance(self, word1: str, word2: str) -> int:
        def helper(word1, word2, i, j, memo):
            if i == len(word1) and j == len(word2):
                return 0
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            
            if (i, j) in memo:
                return memo[(i, j)]
            else:
                if word1[i] == word2[j]:
                    result = helper(word1, word2, i+1, j+1, memo)
                else:
                    insert = 1 + helper(word1, word2, i, j+1, memo)
                    delete = 1 + helper(word1, word2, i+1, j, memo)
                    replace = 1 + helper(word1, word2, i+1, j+1, memo)
                    result = min(insert, delete, replace)
                memo[(i, j)] = result
                return result
        
        return helper(word1, word2, 0, 0, {})
        
class Solution_raw_recursion:
    # will definitely TLE as TC is O(3^max(len(word1), len(word2)))
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 and not word2:
            return 0
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        
        if word1[0] == word2[0]:
            return self.minDistance(word1[1:], word2[1:])
        else:
            insert = 1 + self.minDistance(word1, word2[1:])
            delete = 1 + self.minDistance(word1[1:], word2)
            replace = 1 + self.minDistance(word1[1:], word2[1:])
            return min(insert, delete, replace)
        
class Solution_bottomup_DP:
    # SC can be optimized by just using 2 rows of dp at any time (since next row only needs previous row)
    def minDistance(self, word1, word2):
        """Dynamic programming solution"""
        m = len(word1)
        n = len(word2)
        table = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            table[i][0] = i
        for j in range(n + 1):
            table[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    table[i][j] = table[i - 1][j - 1]
                else:
                    table[i][j] = 1 + min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1])
        return table[-1][-1]