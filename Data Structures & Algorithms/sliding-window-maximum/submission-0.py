class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()

        ans = []
        for idx, num in enumerate(nums):
            if queue and queue[0] < idx - k + 1:
                queue.popleft()
            
            while queue and nums[queue[-1]] <= num:
                queue.pop()

            queue.append(idx)

            if idx >= k-1:
                ans.append(nums[queue[0]])
        
        return ans

