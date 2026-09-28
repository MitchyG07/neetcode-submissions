class Solution:
    def isValid(self, s: str) -> bool:
        sym_map = {'}':'{', ')':'(', ']':'['}
        stack = []
        for c in s:
            if c in sym_map:
                if stack and stack[-1] == sym_map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
            
