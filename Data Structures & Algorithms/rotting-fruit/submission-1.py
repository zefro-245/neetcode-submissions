class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        lrow = len(grid)
        lcol = len(grid[0])

        minutes = 0
        fresh = 0
        q = deque()

        for r in range(lrow):
            for c in range(lcol):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nr >= lrow or nc < 0 or nc >= lcol:
                        continue

                    if grid[nr][nc] != 1:
                        continue

                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc))

            minutes += 1

        if fresh > 0:
            return -1

        return minutes