from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ''' strings are immutable, hence the need to append char by char
        '''
        char_to_idx = {}
        for i, idx in enumerate(indices):
            char_to_idx[idx] = s[i]
        
        out = ''
        for i in range(len(s)):
            out += char_to_idx[i]
            
        return out
            
print(Solution().restoreString('codeleet', [4, 5, 6, 7, 0, 2, 1,3]))
# 'leetcode' 

# alternative solution using list, which is mutable, followed by ''.join()
# def restoreString(self, s: str, indices: List[int]) -> str:
#     A = [''] * len(s)
#     for i, c in zip(indices, s):
#         A[i] = c
#     return "".join(A)

