class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjlist = defaultdict(list)
        for start,destination,price in flights:
            adjlist[start].append((destination,price))
        
        q = deque([(0, src, 0)])
        ans = float('inf')

        mincost = {}

        while q:
            stops,dest,dist = q.popleft()
            
            if (stops,dest) in mincost and mincost[(stops,dest)]<=dist:
                continue
            mincost[(stops,dest)] = dist

            if dest==dst:
                ans = min(dist,ans)
                continue
            if stops==k+1:
                continue
            
            for neidst,neicost in adjlist[dest]:
                q.append((stops+1,neidst,dist+neicost))
        if ans == float('inf'):
            return -1
        return ans
            