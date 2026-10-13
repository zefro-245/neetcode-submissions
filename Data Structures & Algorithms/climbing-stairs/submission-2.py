class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1]*(n+1)
        def f(i):
            if i==0:
                return 1
            if i==1:
                return 1
            
            if dp[i]!=-1:
                return dp[i]

            dp[i-1]=f(i-1)
            dp[i-2]=f(i-2)
            return f(i-1)+f(i-2)

        return f(n)