class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        lrow = len(grid)
        lcol = len(grid[0])
        visit = set()
        q = deque()
        dist = 0

        def addcell(r,c):
            if r<0 or r==lrow or c<0 or c==lcol or (r,c) in visit or grid[r][c]==-1:
                return
            q.append((r,c))
            visit.add((r,c))

        for r in range(lrow):
            for c in range(lcol):
                if grid[r][c]==0:
                    q.append((r,c))
                    visit.add((r,c))
        while q:
            for i in range((len(q))):
                r,c = q.popleft()
                grid[r][c]=dist

                addcell(r+1,c)
                addcell(r-1,c)
                addcell(r,c+1)
                addcell(r,c-1)
            dist+=1
