class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        degree = defaultdict(int)
        adj = defaultdict(list)
        for a, b in edges:
            degree[a]+= 1
            adj[a].append(b)
            degree[b]+= 1
            adj[b].append(a)
        
        queue = deque()
        visited = set()
        for v in degree.keys():
            if degree[v] <= 1:
                queue.append(v)
                visited.add(v)
    
        last_round = []
        while queue:
            last_round = []
            n = len(queue)
            for i in range(n):
                v = queue.popleft()
                visited.add(v)
                last_round.append(v)
                for u in adj[v]:
                    if u not in visited:
                        degree[u] -= 1
                        if degree[u] <= 1:
                            visited.add(u)
                            queue.append(u)
        

        return last_round
