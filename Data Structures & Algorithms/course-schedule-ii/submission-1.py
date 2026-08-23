class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]

        for src, dst in prerequisites:
            adj[dst].append(src)
            indegree[src] += 1

        
        availableClasses = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                availableClasses.append(i)
        
        courses = []

        while availableClasses:
            i = availableClasses.popleft()
            courses.append(i)
            for j in adj[i]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    availableClasses.append(j)
        
        return courses if len(courses) == numCourses else []