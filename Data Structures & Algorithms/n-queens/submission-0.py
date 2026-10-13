class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.']*n for _ in range(n)]
        def isSafe(row,col,board):
            r_row = row
            r_col = col
            while row>=0 and col>=0:
                if board[row][col]=='Q':
                    return False
                row -= 1
                col -= 1

            row = r_row
            col = r_col
            while col>=0:
                if board[row][col]=='Q':
                    return False
                col -= 1

            row = r_row
            col = r_col
            while row<n and col>=0:
                if board[row][col]=='Q':
                    return False
                row += 1
                col -= 1
            
            return True
        
        def dfs(col, board):
            if col==n:
                res.append([''.join(row) for row in board])
                return
            for row in range(n):
                if isSafe(row,col,board):
                    board[row][col] = 'Q'
                    dfs(col+1,board)
                    board[row][col] = '.'
        dfs(0,board)
        return res

