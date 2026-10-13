class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        lrow = len(grid)
        lcol = len(grid[0])
        visit = set()
        q = deque()
        target=0

        def addban(r,c):
            if r<0 or r>=lrow or c<0 or c>=lcol or grid[r][c]==0 or (r,c) in visit:
                return
            grid[r][c] = 2
            nonlocal target
            target-=1
            visit.add((r,c))
            q.append((r,c))

        for r in range(lrow):
            for c in range(lcol):
                if grid[r][c]==1:
                    target+=1
                if grid[r][c]==2:
                    visit.add((r,c))
                    q.append((r,c))
        
        time = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                addban(r+1,c)
                addban(r-1,c)
                addban(r,c+1)
                addban(r,c-1)
            time+=1

        if target>0:
            return -1
        if time:
            return time-1
        else: 
            return 0