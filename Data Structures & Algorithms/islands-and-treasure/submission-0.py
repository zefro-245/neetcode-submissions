class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        lrow = len(grid)
        lcol = len(grid[0])

        q = deque()

        for r in range(lrow):
            for c in range(lcol):
                if grid[r][c] == 0:
                    q.append([r,c])
        
        while q:
            r,c = q.popleft()
            directions = [(1,0),(0,1),(-1,0),(0,-1)]
            for dr,dc in directions:
                nr = r+dr
                nc = c+dc
    
                if nr < 0 or nr >= lrow or nc < 0 or nc >= lcol:
                    continue

                if grid[nr][nc] == -1:
                    continue

                if grid[nr][nc] != 2147483647:
                    continue
            
                grid[nr][nc] = grid[r][c] + 1

                q.append((nr,nc))
        


