class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans <<= 1
            ans += (n % 2)
            n >>= 1
        return ans