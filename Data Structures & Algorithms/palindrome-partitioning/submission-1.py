class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, sol = [], []

        def dfs(start):
            if start >= len(s):
                res.append(sol.copy())
                return
            
            for i in range(start, len(s)):
                if s[start:i+1] and s[start:i+1]==s[start:i+1][::-1]:
                    sol.append(s[start:i+1])
                    dfs(i+1)
                    sol.pop()

        dfs(0)
        return res