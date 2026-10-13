class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, sol = [], ""
        open, close = 0, 0
        def dfs():
            nonlocal sol
            nonlocal open
            nonlocal close
            if len(sol)==2*n:
                res.append(sol)
                return
            
            if open < n:
                sol += "("
                open += 1
                dfs()
                sol = sol[:-1]
                open -= 1
            if close < open:
                sol += ")"
                close += 1
                dfs()
                sol = sol[:-1]
                close -= 1

        dfs()
        return res