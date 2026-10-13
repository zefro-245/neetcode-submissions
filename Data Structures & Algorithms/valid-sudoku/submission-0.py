class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            seen = set()
            for num in i:
                if num == ".":
                    continue

                if num in seen:
                    return False
                seen.add(num)

        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in seen:
                    return False
                else:
                    seen.add(board[j][i])
        for box_row in range(0,9,3):
            for box_col in range(0,9,3):
                seen = set()
                for i in range(0,3):
                    for j in range(0,3):
                        if board[box_row+i][box_col+j] == ".":
                            continue
                        if board[box_row+i][box_col+j] in seen:
                            return False
                        else:
                            seen.add(board[box_row+i][box_col+j])
        return True

        