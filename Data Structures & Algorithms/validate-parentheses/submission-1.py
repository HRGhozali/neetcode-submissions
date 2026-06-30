class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {'[':']', '(':')','{':'}'}
        for char in s:
            match char:
                case item if item in match:
                    stack.append(char)
                case _:
                    if len(stack) == 0: return False
                    if match[stack[-1]] != char: return False
                    stack.pop()
        if len(stack) > 0: return False
        return True