class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        dp = [[0] * (amount + 1) for _ in range(n)]

        for T in range(amount + 1):
            if T % coins[0] == 0:
                dp[0][T] = 1

        for ind in range(1,n):
            for T in range(amount + 1):
                notTake = dp[ind - 1][T]

                take = 0
                if coins[ind] <= T:
                    take = dp[ind][T - coins[ind]]

                dp[ind][T] = take + notTake

        return dp[n - 1][amount]

