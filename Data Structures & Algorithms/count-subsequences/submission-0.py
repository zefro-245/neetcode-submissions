class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[-1]*len(t) for _ in range(len(s))]

        def f(i,j):
            if j==len(t):
                return 1
            if i==len(s):
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if s[i] == t[j]:
                dp[i][j] = f(i+1,j+1) + f(i+1,j)
            else:
                dp[i][j] = f(i+1,j)
            
            return dp[i][j]
        return f(0,0)