class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [-1]*(n)
        
        def f(i):
            if i==len(s):
                return 1
            if int(s[i])==0:
                return 0
            if dp[i]!=-1:
                return dp[i]
            dp[i] = f(i+1)
            if i+1<len(s) and 10<=int(s[i]+s[i+1])<=26:
                dp[i] += f(i+2)

            return dp[i]
        
        return f(0)