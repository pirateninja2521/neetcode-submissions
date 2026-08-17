class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for _, cnt in Counter(nums).items():
            if cnt > 1: return True
        return False