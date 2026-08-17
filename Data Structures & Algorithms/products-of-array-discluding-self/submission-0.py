class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        prefix_mult = [ 1 ]
        suffix_mult = [ 1 ]
        for i in range(0, N):
            prefix_mult.append(prefix_mult[i] * nums[i])
            suffix_mult.append(suffix_mult[i] * nums[N-1-i])
        
        return [ prefix_mult[i] * suffix_mult[N - i - 1] for i in range(N)]