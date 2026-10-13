class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxcount = 0
        lrow = len(grid)
        lcol = len(grid[0])

        def dfs(r,c):
            nonlocal count
            if r<0 or r>=lrow or c<0 or c>=lcol:
                return
            if grid[r][c] == 0:
                return

            grid[r][c] = 0
            count += 1

            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)
        
        for r in range(lrow):
            for c in range(lcol):
                if grid[r][c] == 1:
                    count = 0
                    dfs(r,c)
                    if maxcount <= count:
                        maxcount = count
        return maxcount