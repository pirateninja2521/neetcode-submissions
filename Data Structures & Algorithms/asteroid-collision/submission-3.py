class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
                continue
            
            broke = False
            while stack and stack[-1] > 0:
                if abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                    broke = True
                    break
                elif abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                else:
                    broke = True
                    break
            if not broke:
                stack.append(asteroid)
            
        return stack
                