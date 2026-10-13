class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*numCourses
        adjlist = [[] for _ in range(numCourses)]
        for a,b in prerequisites:
            indegree[b]+=1 # a->b
            adjlist[a].append(b) # b is the prereq for a so a->b

        q = deque()
        for n in range(numCourses):
            if indegree[n]==0:
                q.append(n)
        
        finish = 0
        while q:
            node = q.popleft()
            finish+=1
            for nei in adjlist[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        return finish==numCourses

        

        

            