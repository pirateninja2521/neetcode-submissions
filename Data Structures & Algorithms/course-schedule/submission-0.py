class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]

        for src, dst in prerequisites:
            adj[src].append(dst)
            indegree[dst] += 1

        
        availableClasses = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                availableClasses.append(i)
        
        finished = 0

        while availableClasses:
            i = availableClasses.popleft()
            finished += 1
            for j in adj[i]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    availableClasses.append(j)
        
        return finished == numCourses