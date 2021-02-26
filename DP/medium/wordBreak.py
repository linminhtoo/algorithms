from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set() # for O(1) find
        for word in wordDict:
            words.add(word)
            
        # catsanddog {'cat', 'cats', 'and', 'dog'} 
        # naive greedy will fail since we will choose cat but there is a hanging s
        
        def helper(start, memo):
            if start >= len(s):
                return True
            
            if start in memo:
                return memo[start]
            else:
                found = False
                for end in range(start + 1, len(s) + 1):
                    if s[start:end] in words:
                        res = helper(end, memo)
                        if res:
                            found = True
                            break
                if found:
                    memo[start] = True
                    return True
                else:
                    memo[start] = False
                    return False
        
        # note: memo can just be a fixed length List also
        return helper(0, {})
                        