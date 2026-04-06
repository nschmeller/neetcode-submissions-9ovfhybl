class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ('(', '{', '['):
                stack.append(c)
            elif not stack:
                return False
            else:
                popped = stack.pop()
                if c == ')' and popped != '(':
                    return False
                elif c == '}' and popped != '{':
                    return False
                elif c == ']' and popped != '[':
                    return False
        return not stack
