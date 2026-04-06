class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: (abs(x) // abs(y)) * (1 if x * y >= 0 else -1),
        }
        stack = []

        for token in tokens:
            if token in ops:
                y, x = stack.pop(), stack.pop()
                stack.append(ops[token](x, y))
            else:
                stack.append(int(token))
        
        return stack[0]
