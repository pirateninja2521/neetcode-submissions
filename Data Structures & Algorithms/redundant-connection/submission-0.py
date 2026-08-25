class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges))]

        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
        
        def union(i, j):
            parent[find(i)] = parent[find(j)]

        for x, y in edges:
            x, y = x-1, y-1
            if find(x) == find(y):
                return [x+1, y+1]
            union(x, y)