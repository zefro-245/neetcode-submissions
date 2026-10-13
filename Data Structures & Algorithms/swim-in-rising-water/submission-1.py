class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        import heapq

        lrow = len(grid)
        lcol = len(grid[0])

        graph = defaultdict(list)

        for r in range(lrow):
            for c in range(lcol):
                if r+1<lrow:
                    graph[(r,c)].append((grid[r+1][c],r+1,c))
                if r-1>=0:
                    graph[(r,c)].append((grid[r-1][c],r-1,c))
                if c+1<lcol:
                    graph[(r,c)].append((grid[r][c+1],r,c+1))
                if c-1>=0:
                    graph[(r,c)].append((grid[r][c-1],r,c-1))
                
        mintimes = {}
        minheap = [(grid[0][0],0,0)]

        while minheap:
            curr_cost,x,y = heapq.heappop(minheap)

            if (x,y) in mintimes:
                continue
            mintimes[(x,y)]=curr_cost

            if (x,y)==(lrow-1,lcol-1):
                return curr_cost
            
            for nei_cost,neix,neiy in graph[(x,y)]:
                if (neix,neiy) not in mintimes:
                    new_cost = max(nei_cost,curr_cost)
                    heapq.heappush(minheap,(new_cost,neix,neiy))
            