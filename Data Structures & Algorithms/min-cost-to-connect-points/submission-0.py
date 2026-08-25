class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        startingPoint = points[0]
        visited = set()
        visited.add(tuple(startingPoint))

        def dist(a, b):
            return abs(a[0]-b[0]) + abs(a[1]-b[1])
        
        availableEdges = [(dist(point, startingPoint), point) for point in points[1:]]
        heapq.heapify(availableEdges)

        totalCost = 0
        while availableEdges:
            cost, point = heapq.heappop(availableEdges)

            if tuple(point) in visited:
                continue
            
            visited.add(tuple(point))
            totalCost += cost

            for nextPoint in points:
                if tuple(nextPoint) not in visited:
                    heapq.heappush(availableEdges, (dist(point, nextPoint), nextPoint))
        
        return totalCost
