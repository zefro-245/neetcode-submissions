class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(open, close, sol):
            if open == n and close == n:
                res.append(sol)
                return

            if open < n:
                dfs(open + 1, close, sol + '(')

            if close < open:
                dfs(open, close + 1, sol + ')')

        dfs(0, 0, '')
        return res