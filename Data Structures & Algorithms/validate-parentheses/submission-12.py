class Solution:
    def isValid(self, s: str) -> bool:
        char_map = {'}':'{', ']':'[',')':'('}
        stack = []
        for char in s:
            if char in char_map.values():
                stack.append(char)
            elif stack and char_map[char] == stack[-1]:
                stack.pop()
            else:
                return False
        return True if not stack else False