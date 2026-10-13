class Solution:
    def solve(self, board: List[List[str]]) -> None:
        lrow = len(board)
        lcol = len(board[0])

        def dfs(r,c):
            if r<0 or r>=lrow or c<0 or c>=lcol:
                return
            if board[r][c] != 'O':
                return
            
            board[r][c] = 'S'
            
            directions = [(0,1),(1,0),(0,-1),(-1,0)]

            for dr,dc in directions:
                nr = r + dr
                nc = c + dc
                dfs(nr,nc)

        for r in range(lrow):
            dfs(r, 0)
            dfs(r, lcol - 1)

        for c in range(lcol):
            dfs(0, c)
            dfs(lrow - 1, c)
        

        for r in range(lrow):
            for c in range(lcol):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"