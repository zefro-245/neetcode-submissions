class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        lrow = len(grid)
        lcol = len(grid[0])
        count = 0
        maxarea = 0
        area = 0
        

        def dfs(r,c):
            if r<0 or r>=lrow or c<0 or c>=lcol:
                return
            if grid[r][c]==0:
                return
            grid[r][c]=0
            nonlocal area
            area+=1
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for r in range(lrow):
            for c in range(lcol):
                if grid[r][c]==1:
                    area=0
                    dfs(r,c)
                    maxarea=max(area,maxarea)
        return maxarea