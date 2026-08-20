class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distAndPoints = [(x**2 + y**2, [x, y]) for x, y in points]

        heapq.heapify(distAndPoints)

        ans = []
        for i in range(k):
            _, point = heapq.heappop(distAndPoints)
            ans.append(point)
        
        return ans


        