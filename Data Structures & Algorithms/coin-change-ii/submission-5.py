class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[-1]*(amount+1) for _ in range(n)]
        def f(i,target):
            if target==0:
                return 1
            if i==n:
                return 0
            
            if dp[i][target]!=-1:
                return dp[i][target]

            
            not_take = f(i+1,target)
            take = 0
            if target>=coins[i]:
                take = f(i,target-coins[i])
            dp[i][target] = take+not_take
            return take+not_take
        
        return f(0,amount)