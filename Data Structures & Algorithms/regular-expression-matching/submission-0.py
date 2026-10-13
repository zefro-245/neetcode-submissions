class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[-1]*len(p) for _ in range(len(s))]

        def f(i,j):
            if i < 0:
                while j >= 1:
                    if p[j] != '*':
                        return False
                    j -= 2
                return j == -1
            if j<0:
                return False
            
            if dp[i][j] !=-1:
                return dp[i][j]
            if s[i]==p[j] or p[j]=='.':
                dp[i][j] = f(i-1,j-1)
            elif p[j] == '*':
                if p[j-1] == s[i] or p[j-1] == '.':
                    dp[i][j] = f(i, j-2) or f(i-1, j)
                else:
                    dp[i][j] = f(i, j-2)
            else:
                dp[i][j] = False
            return dp[i][j]
        return f(len(s)-1,len(p)-1)