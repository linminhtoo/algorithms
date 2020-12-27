class Solution():
    def checkPermutation(self, stringA: str, stringB: str):
        stringA, stringB = stringA.lower(), stringB.lower() 
        if set(stringA).symmetric_difference(set(stringB)): # strings have different characters in them
            return False
        return True
    
print(Solution().checkPermutation('abcd', 'bcda'))
# True
