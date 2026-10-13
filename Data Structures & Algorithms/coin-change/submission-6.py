class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [float('inf')]*(amount+1)
        dp[0]=0

        for i in range(1,amount+1):
            for c in coins:
                if i>=c:
                    dp[i] = min(dp[i],1+dp[i-c])

        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]