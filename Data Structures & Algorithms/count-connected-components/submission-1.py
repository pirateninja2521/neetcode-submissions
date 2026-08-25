class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        components = n
        
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
        
        def union(i, j):
            parent[find(i)] = parent[find(j)]

        for x, y in edges:
            if find(x) == find(y):
                continue
            components -= 1
            union(x, y)
        return components
