class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        lrow = len(heights)
        lcol = len(heights[0])
        pacific = [[False] * lcol for _ in range(lrow)]
        atlantic = [[False] * lcol for _ in range(lrow)]

        def dfs(r,c,ocean):
            if r<0 or r>=lrow or c<0 or c>=lcol:
                return
            if ocean[r][c]:
                return
            
            ocean[r][c] = True
            
            directions = [(0,1),(1,0),(0,-1),(-1,0)]

            for dr,dc in directions:
                nr = r+dr
                nc = c+dc
                if (0<=nr<lrow) and (0<=nc<lcol) and (heights[nr][nc] >= heights[r][c]):
                    dfs(nr,nc,ocean) 

        for r in range(lrow):
            dfs(r,0,pacific)
        for c in range(lcol):
            dfs(0,c,pacific)
        for r in range(lrow):
            dfs(r,lcol-1,atlantic)
        for c in range(lcol):
            dfs(lrow-1,c,atlantic)  

        for r in range(lrow):
            for c in range(lcol):
                if pacific[r][c] and atlantic[r][c]:
                    res.append([r,c])      
        return res