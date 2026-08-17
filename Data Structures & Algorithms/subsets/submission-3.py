class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        ans = []
        for i in range(2**N):
            temp = []
            for index, num in enumerate(nums):
                if i & (1 << index):
                    temp.append(num)
            ans.append(temp)
        return ans