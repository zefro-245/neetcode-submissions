class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        dp = [[-1] * (amount + 1) for _ in range(n)]

        def f(ind, T):
            if ind == 0:
                if T % coins[0] == 0:
                    return 1
                return 0

            if dp[ind][T] != -1:
                return dp[ind][T]

            notTake = f(ind - 1, T)

            take = 0
            if coins[ind] <= T:
                take = f(ind, T - coins[ind])

            dp[ind][T] = take + notTake

            return dp[ind][T]

        ans = f(n - 1, amount)

        return -1 if ans == float('inf') else ans