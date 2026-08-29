class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target <= nums[0]: return 0
        if target > nums[-1]: return len(nums)

        l = 0
        r = len(nums)

        while (l <= r):
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target <= nums[mid+1]:
                return mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
                
        