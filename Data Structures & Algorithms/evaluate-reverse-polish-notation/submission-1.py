class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                right, left = stack.pop(), stack.pop()
                stack.append(left + right)
            elif token == '-':
                right, left = stack.pop(), stack.pop()
                stack.append(left - right)
            elif token == '*':
                right, left = stack.pop(), stack.pop()
                stack.append(left * right)
            elif token == '/':
                right, left = stack.pop(), stack.pop()
                stack.append(int(float(left) / right))
            else:
                stack.append(int(token))
        return stack[0]
