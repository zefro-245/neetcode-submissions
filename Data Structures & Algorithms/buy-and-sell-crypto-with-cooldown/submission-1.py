class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1] * 2 for _ in range(n + 1)]

        def f(ind, buy):
            if ind>=n:
                return 0
            if dp[ind][buy] != -1:
                return dp[ind][buy]
            if buy:
                dp[ind][buy] = max(-prices[ind]+f(ind+1,0),f(ind+1,1))
            else:
                dp[ind][buy] = max(prices[ind]+f(ind+2,1),f(ind+1,0))
            return dp[ind][buy]
        
        return f(0,1)