class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res,sol = [], ''
        open,close = 0,0
        def dfs(open,close,sol):
            if open==n and close==n:
                res.append(sol)
                return
            if open<n:
                sol +='('
                open+=1
                dfs(open,close,sol)
                sol=sol[:-1]
                open-=1

            if close<open:
                sol += ')'
                close+=1
                dfs(open,close,sol)
        dfs(open,close,sol)
        return res