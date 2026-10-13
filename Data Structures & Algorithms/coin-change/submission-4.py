class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [-1]*(amount+1)
        def f(rem):
            prev = float('inf')
            if rem==0:
                return 0
            if rem<0:
                return float('inf')
            if dp[rem] != -1:
                return dp[rem]
            for j in range(len(coins)):
                way = 1+f(rem-coins[j])
                prev = min(prev,way)
                dp[rem] = prev

            return prev
        
        if f(amount) == float('inf'):
            return -1
        else:
            return f(amount)