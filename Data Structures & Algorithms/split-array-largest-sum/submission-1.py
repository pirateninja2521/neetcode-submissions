class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
            
        def canSplit(target) -> bool:
            currentSum = 0
            splits = 1
            for num in nums:
                currentSum += num
                if currentSum > target:
                    splits += 1
                    currentSum = num
                    if splits > k:
                        return False
            return True
        
        l = max(nums)
        r = sum(nums)
        ans = 0
        while l <= r:
            mid = (l + r)//2

            if canSplit(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans

        