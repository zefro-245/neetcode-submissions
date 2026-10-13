class Solution:
    def solve(self, board: List[List[str]]) -> None:
        lrow = len(board)
        lcol = len(board[0])

        q = deque()
        seen = set()

        for i in range(0,lrow):
            if board[i][0]=='O':
                q.append((i,0))
                seen.add((i,0))
        for i in range(1,lcol):
            if board[0][i]=='O':
                q.append((0,i))
                seen.add((0,i))
        for i in range(1,lrow):
            if board[i][lcol-1]=='O':
                q.append((i,lcol-1))
                seen.add((i,lcol-1))
        for i in range(1,lcol-1):
            if board[lrow-1][i]=='O':
                q.append((lrow-1,i))
                seen.add((lrow-1,i))
        
        while q:
            r,c = q.popleft()
            direc = [(0,1),(0,-1),(1,0),(-1,0)]
            for dr,dc in direc:
                i,j = r+dr, c+dc
                if 0<=i<lrow and 0<=j<lcol and (i,j) not in seen and board[i][j]=='O':
                    seen.add((i,j))
                    q.append((i,j))
        
        for r in range(lrow):
            for c in range(lcol):
                if (r,c) not in seen and board[r][c]=='O':
                    board[r][c]='X'

