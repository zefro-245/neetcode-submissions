class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        lrow = len(grid)
        lcol = len(grid[0])
        count = 0

        def dfs(r,c):
            if r<0 or r>=lrow or c<0 or c>=lcol:
                return
            if grid[r][c]=="0":
                return
            grid[r][c]="0"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for r in range(lrow):
            for c in range(lcol):
                if grid[r][c]=="1":
                    count+=1
                    dfs(r,c)
        return count
        