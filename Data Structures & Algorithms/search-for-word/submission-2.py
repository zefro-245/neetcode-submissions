class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r,c,i):
            if i==len(word):
                return True
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return False
            direc = [(0,1),(1,0),(-1,0),(0,-1)]
            if board[r][c]==word[i]:
                board[r][c]='#'
                for dr,dc in direc:
                    nr=r+dr
                    nc=c+dc
                    if dfs(nr,nc,i+1):
                        board[r][c]=word[i]
                        return True
                board[r][c]=word[i]
                return False


        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r,c,0):
                    return True
        return False