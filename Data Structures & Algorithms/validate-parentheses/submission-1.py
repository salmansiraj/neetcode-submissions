class Solution:
    def isValid(self, s: str) -> bool:
        closed = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        
        stack = []
        for c in s:
            if len(stack) == 0 or c not in closed:
                stack.append(c)
            elif c in closed and closed[c] == stack[-1]:
                stack.pop()
            else:
                return False
        print(stack)
        return True if len(stack) == 0 else False
            