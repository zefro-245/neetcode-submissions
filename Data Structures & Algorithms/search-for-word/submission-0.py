class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        sol = ""
        visited = [[False] * len(board[0]) for _ in range(len(board))]
        rows = len(board)
        cols = len(board[0])
        def dfs(r,c,i):
            if i==len(word):
                return True
            
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            
            if board[r][c] != word[i]:
                return False

            
            if visited[r][c]:
                return False

            visited[r][c] = True

            found = (dfs(r+1, c, i+1)   or
            dfs(r-1, c, i+1)  or
            dfs(r, c+1, i+1)  or
            dfs(r, c-1, i+1))

            visited[r][c] = False

            return found
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False

