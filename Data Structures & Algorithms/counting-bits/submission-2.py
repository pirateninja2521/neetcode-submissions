class Solution:
    def countBits(self, n: int) -> List[int]:
        stack = []
        ret = [0]
        for i in range(n):
            
            toPush = 1
            while stack and stack[-1] == toPush:
                toPush += stack.pop()
            stack.append(toPush)
            ret.append(len(stack))
        return ret
        