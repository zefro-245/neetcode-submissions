class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []
        indegree = [0]*numCourses
        adjlist = [[] for _ in range(numCourses)]
        for a,b in prerequisites:
            indegree[a]+=1 #a->b
            adjlist[b].append(a)
        
        q = deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        
        finish = 0
        while q:
            node = q.popleft()
            ans.append(node)
            finish+=1
            for nei in adjlist[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        if finish!=numCourses:
            return []
        else:
            return ans


