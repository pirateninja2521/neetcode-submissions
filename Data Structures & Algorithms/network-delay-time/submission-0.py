class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adjList = {}
        for u, v, t in times:
            if u not in adjList:
                adjList[u] = []
            adjList[u].append([v, t])

        
        nodes = [(0, k)]
        distance = {}
        while nodes:
            time, node = heapq.heappop(nodes)
            if node in distance:
                # visited before with shorted length
                continue
            distance[node] = time
            for v, t in adjList.get(node, []):
                if v not in distance:
                    heapq.heappush(nodes, [time + t, v])
        
        if len(distance) < n:
            return -1
        return max(distance.values())
