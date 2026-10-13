class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        lrow = len(heights)
        lcol = len(heights[0])

        a_q = deque()
        a_vis = set()

        p_q = deque()
        p_vis = set()

        for i in range(lcol):
            p_q.append((0,i))
            p_vis.add((0,i))
        for i in range(1,lrow):
            p_q.append((i,0))
            p_vis.add((i,0))
        
        for j in range(lcol):
            a_q.append((lrow-1,j))
            a_vis.add((lrow-1,j))
        for j in range(lrow-1):
            a_q.append((j,lcol-1))
            a_vis.add((j,lcol-1))
        
        def check(q,seen):
            while q:
                i,j = q.popleft()

                for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                    r,c = i+dr, j+dc
                    if 0<=r<lrow and 0<=c<lcol and heights[r][c]>=heights[i][j] and (r,c) not in seen:
                        seen.add((r,c))
                        q.append((r,c))
            return seen
        
        p_coords = check(p_q,p_vis)
        a_coords = check(a_q,a_vis)
    
        return list(p_coords.intersection(a_coords))
                
