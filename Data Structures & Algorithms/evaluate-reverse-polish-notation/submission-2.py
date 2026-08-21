class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            if tok not in ['+', '-', '*', '/']:
                stack.append(int(tok))
            else:
                n2 = stack.pop()
                n1 = stack.pop()
                if tok == '+':
                    stack.append(n1 + n2)
                elif tok == '-':
                    stack.append(n1 - n2)
                elif tok == '*':
                    stack.append(n1 * n2)
                else:
                    stack.append(int(n1 / n2))
        return stack[-1]