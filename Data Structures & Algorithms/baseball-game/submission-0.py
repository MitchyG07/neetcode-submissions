class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for o in operations:
            if o == '+':
                score = stack[-1] + stack[-2]
                stack.append(score)
            elif o == 'D':
                stack.append(stack[-1] * 2)
            elif o == 'C':
                stack.pop()
            else:
                stack.append(int(o))
            
        total_score = sum(stack)
        return total_score