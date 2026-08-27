class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == "+":
                record = stack[-1] + stack[-2]
                stack.append(record)
            elif op == "C":
                stack.pop()
            elif op == "D":
                record = stack[-1] * 2
                stack.append(record)
            else:
                stack.append(int(op))
        return sum(stack)
        