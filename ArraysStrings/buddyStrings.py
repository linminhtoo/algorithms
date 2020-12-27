# https://leetcode.com/problems/buddy-strings/submissions/
# 38% faster, 100% less 

class Solution_slower:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) == 1 or len(B) == 1:
            return False
        # don't actually need, because covered by code just below
        
        if A == B:
            set_A = set()
            for letter in A:
                if letter in set_A:
                    return True
                set_A.add(letter)
            return False
            
        if len(A) != len(B):
            return False
        
        A_set, B_set = set(), set()
        for letter in A:
            A_set.add(letter)
        for letter in B:
            if letter not in A_set:
                return False
        
        counter, mismatch_dict = 0, {}
        for i, (letter_A, letter_B) in enumerate(zip(A, B)):
            if letter_A != letter_B:
                counter += 1
                mismatch_dict[letter_B] = letter_A
            
            if counter == 2:
                if letter_A not in mismatch_dict.keys():
                    return False
                elif mismatch_dict[letter_A] != letter_B:
                    return False
            
            if counter > 2:
                return False
            
        return True

# 70% faster, 100% less
class Solution_faster:
    def buddyStrings(self, A: str, B: str) -> bool:       
        if A == B:
            set_A = set()
            for letter in A:
                if letter in set_A:
                    return True
                set_A.add(letter)
            return False
            
        if len(A) != len(B):
            return False
        
        counter, mismatch_dict = 0, {}
        for i, (letter_A, letter_B) in enumerate(zip(A, B)):
            if letter_A != letter_B:
                counter += 1
                mismatch_dict[letter_B] = letter_A
            
            if counter == 2:
                if letter_A not in mismatch_dict.keys():
                    return False
                elif mismatch_dict[letter_A] != letter_B:
                    return False
            
            if counter > 2:
                return False
            
        if counter == 1: # need this when the two strings differ by just a letter 
            return False
        return True
                
                
            