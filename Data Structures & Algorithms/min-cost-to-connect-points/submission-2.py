class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        import heapq
        minheap = [[0,0]]
        res = 0
        visit = set()

        N = len(points)
        adj = {i:[] for i in range(N)}
        for i in range(N):
            x1,y1 = points[i]
            for j in range(i+1,N):
                dist = abs(x1-points[j][0])+abs(y1-points[j][1])
                adj[i].append([dist,j])
                adj[j].append([dist,i])
            
        while len(visit)<N:
            cost,i = heapq.heappop(minheap)

            if i in visit:
                continue
            res+=cost
            visit.add(i)

            for neiCost,nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minheap,(neiCost,nei))
        return res