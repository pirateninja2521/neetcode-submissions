class MedianFinder:

    def __init__(self):
        # max-heap with negative val
        self.lowerHalf = []
        # min-heap
        self.upperHalf = []

    def addNum(self, num: int) -> None:
        low = - self.lowerHalf[0] if self.lowerHalf else float("-inf")
        high = self.upperHalf[0] if self.upperHalf else float("inf")
        if num < low:
            heapq.heappush(self.lowerHalf, -num)
            if len(self.lowerHalf) > len(self.upperHalf):
                tmp = heapq.heappop(self.lowerHalf)
                heapq.heappush(self.upperHalf, -tmp)
        else:
            heapq.heappush(self.upperHalf, num)
            if len(self.lowerHalf) + 1 < len(self.upperHalf):
                tmp = heapq.heappop(self.upperHalf)
                heapq.heappush(self.lowerHalf, -tmp)
        

        


    def findMedian(self) -> float:
        if (len(self.lowerHalf) < len(self.upperHalf)):
            return self.upperHalf[0]
        return (self.upperHalf[0] - self.lowerHalf[0]) / 2
        