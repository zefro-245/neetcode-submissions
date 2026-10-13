class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1]*2 for _ in range(n)]
        def f(i, buy):
            if i>=n:
                return 0
            if dp[i][buy]!=-1:
                return dp[i][buy]
            if buy:
                dp[i][buy] = max(-prices[i]+f(i+1,0),f(i+1,1))
                return max(-prices[i]+f(i+1,0),f(i+1,1))
            else:
                dp[i][buy] = max(prices[i]+f(i+2,1),f(i+1,0))
                return max(prices[i]+f(i+2,1),f(i+1,0))
        
        return f(0,1)