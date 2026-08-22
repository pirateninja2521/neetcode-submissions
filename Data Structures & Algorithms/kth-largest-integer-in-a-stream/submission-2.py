class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for num in nums:
            if len(self.heap) < self.k:
                heapq.heappush(self.heap, num)
            else:
                if num < self.heap[0]:
                    continue
                else:
                    heapq.heappushpop(self.heap, num)       

    def add(self, val: int) -> int:
        if self.heap and val < self.heap[0]:
            return self.heap[0]
        else:
            heapq.heappush(self.heap, val)
            if len(self.heap) > self.k:
                heapq.heappop(self.heap)
            return self.heap[0]
        
