class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for start,dest,price in flights:
            graph[start].append((dest,price))
        
        q = deque([(0,src,0)])
        ans = float("inf")

        mincost = {}

        while q:
            stops,destination,price = q.popleft()

            state = (stops, destination)

            if state in mincost and mincost[state] <= price:
                continue

            mincost[state] = price
            
            if destination == dst:
                ans = min(price,ans)
                continue
            if stops == k+1:
                continue

            for nei_dest,nei_price in graph[destination]:
                new_price = price + nei_price
                q.append((stops+1,nei_dest,new_price))
        if ans == float("inf"):
            return -1
        else:
            return ans
