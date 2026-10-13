class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, sol = [], []
        n = len(s)

        def dfs(i,sol):
            if i==n:
                res.append(sol.copy())
                return
            for j in range(i,n):
                if s[i:j+1]==s[i:j+1][::-1]:
                    sol.append(s[i:j+1])
                    dfs(j+1,sol)
                    sol.pop()
        dfs(0,sol)
        return res