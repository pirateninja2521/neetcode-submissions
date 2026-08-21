class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        def match(c1, c2):
            return [c1, c2] in [['(', ')'], ['{', '}'], ['[', ']']]
        for char in s:
            if stack and match(stack[-1], char):
                stack.pop()
            else: stack.append(char)
        
        return False if stack else True
        