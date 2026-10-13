class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]

        for a,b in prerequisites:
            graph[b].append(a)
            
        path = set()
        def dfs(course):
            if course in path:
                return False
            if graph[course] == []:
                return True
            path.add(course)

            for neighbour in graph[course]:
                if not dfs(neighbour):
                    return False
            path.remove(course)
            graph[course] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True