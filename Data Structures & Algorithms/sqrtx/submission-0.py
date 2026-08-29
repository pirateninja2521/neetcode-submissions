class Solution:
    def mySqrt(self, x: int) -> int:
        root = 0
        while ((root + 1)**2 <= x):
            root += 1
        return root
        