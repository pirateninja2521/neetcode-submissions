class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        curLoad = 0
        
        # sort by from 
        trips.sort(key=lambda t:t[1])

        minHeap = []

        for numPass, start, end in trips:
            while minHeap and minHeap[0][0] <= start:
                curLoad -= heapq.heappop(minHeap)[1]
            
            curLoad += numPass
            if curLoad > capacity:
                return False
            
            heapq.heappush(minHeap, [end, numPass])
        
        return True

