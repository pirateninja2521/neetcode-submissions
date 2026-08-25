class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        unionFind = [i for i in range(n)]
        def find(i):
            if unionFind[i] == i:
                return i
            unionFind[i] = find(unionFind[i])
            return unionFind[i]
        def union(i, j):
            unionFind[find(i)] = find(j)

        for edge in edges:
            x, y = edge
            if find(x) == find(y):
                return False
            union(x, y)

        return True        
