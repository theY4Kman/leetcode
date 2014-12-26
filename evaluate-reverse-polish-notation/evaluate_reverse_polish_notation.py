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

    tests = [
        (["10","6","9","3","+","-11","*","/","*","17","+","5","+"],
            22),
        (["2", "1", "+", "3", "*"],
            9),
        (["4", "13", "5", "/", "+"],
            6),
    ]
