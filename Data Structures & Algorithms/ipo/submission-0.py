class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        allProjects = [[cap, profit] for cap, profit in zip(capital, profits)]
        available = []

        heapq.heapify(allProjects)

        for i in range(k):
            while allProjects and allProjects[0][0] <= w:
                cap, profit = heapq.heappop(allProjects)
                heapq.heappush_max(available, profit)
            
            if not available:
                return w
            
            w += heapq.heappop_max(available)
        
        return w