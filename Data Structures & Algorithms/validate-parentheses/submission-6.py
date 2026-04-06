class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ("(", "{", "["):
                stack.append(c)
            else:
                if not stack:
                    return False
                popped = stack.pop()
                if (c == ")" and popped != "(" or 
                   c == "}" and popped != "{" or
                   c == "]" and popped != "["):
                    return False

        return not stack
