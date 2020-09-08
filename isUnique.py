class Solution():
    def isUnique(self, string: str):
        '''Checks whether a given string has unique characters only
        
        Inputs
        ------
        string: str
            string to be checked for unique chars

        Assumptions
        ------------
        Whitespace ' ' is a character
        String is in ASCII-128

        Returns
        -------
        bool
            whether string has unique chars only

        '''
        if len(string) > 128: 
            return False
        
        seen_chars = set()
        for char in string:
            if char in seen_chars:
                return False
            seen_chars.add(char)
        return True

print(Solution().isUnique('the quick brown'))
# False
print(Solution().isUnique('the quickbrown'))
# True
