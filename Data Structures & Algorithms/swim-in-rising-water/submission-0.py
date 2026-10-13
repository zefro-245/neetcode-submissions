class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        import heapq
        graph = defaultdict(list)
        lrow = len(grid)
        lcol = len(grid[0])
        for row in range(lrow):
            for coloumn in range(lcol):
                if (row+1)<lrow:
                    graph[(row,coloumn)].append((grid[row+1][coloumn],row+1,coloumn))
                if (row-1)>=0:
                    graph[(row,coloumn)].append((grid[row-1][coloumn],row-1,coloumn))
                if (coloumn+1)<lcol:
                    graph[(row,coloumn)].append((grid[row][coloumn+1],row,coloumn+1))
                if (coloumn-1)>=0:
                    graph[(row,coloumn)].append((grid[row][coloumn-1],row,coloumn-1))
        
        mintimes = {}
        minheap = [(grid[0][0],0,0)]

        while minheap:
            curr_cost,x,y = heapq.heappop(minheap)

            if (x,y) in mintimes:
                continue
            
            mintimes[(x,y)] = curr_cost

            if (x,y) == (lrow-1,lcol-1):
                return curr_cost
            for nei_cost, neix, neiy in graph[(x,y)]:
                if (neix,neiy) not in mintimes:
                    newcost = max(nei_cost,curr_cost)
                    heapq.heappush(minheap, (newcost,neix,neiy))

