class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        ops = {
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(float(a) / b),
            '-': lambda a, b: a - b,
            '+': lambda a, b: a + b,
        }
        stack = []
        for token in tokens:
            if token in ops:
                b = stack.pop()
                a = stack.pop()
                stack.append(ops[token](a, b))
            else:
                stack.append(int(token))
        return stack[-1]
