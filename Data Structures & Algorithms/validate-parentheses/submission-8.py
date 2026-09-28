class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        validMap = {
            '}':'{',
            ')':'(',
            ']':'['
        }
        #edge case
        n = len(s)
        if n <= 1:
            return False 

        for char in s:
            #if open parentheses
            if char in validMap.values():
                if char not in stack:
                    stack.append(char)
                    continue
                else:
                    return False
            #if closed parentheses
            if validMap[char] in stack and stack[-1] == validMap[char]:
                stack.pop()
                continue
            
            return False
        
        if len(stack):
            return False
        else:
            return True