class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        
        stack = []
        
        for char in s:
            if char in ["[", "{", "("]:
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if char == "]" and top != "[":
                    return False
                if char == "}" and top != "{":
                    return False
                if char == ")" and top != "(":
                    return False
        
        return not stack