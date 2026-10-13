class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        for a,b in prerequisites:
            g[a].append(b)
        
        UNVISITED, VISITING, VISITED = 0, 1, 2
        states = [UNVISITED]*numCourses

        def dfs(i):
            if states[i] == VISITING:
                return False
            elif states[i] == VISITED:
                return True
            states[i] = VISITING

            for nei in g[i]:
                if not dfs(nei):
                    return False
            states[i] = VISITED
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
        