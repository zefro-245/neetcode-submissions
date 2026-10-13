class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        dp = [[-1] * (amount + 1) for _ in range(n)]

        def f(ind, T):
            if ind == 0:
                if T % coins[0] == 0:
                    return T // coins[0]
                return float('inf')

            if dp[ind][T] != -1:
                return dp[ind][T]

            notTake = f(ind - 1, T)

            take = float('inf')
            if coins[ind] <= T:
                take = 1 + f(ind, T - coins[ind])

            dp[ind][T] = min(take, notTake)

            return dp[ind][T]

        ans = f(n - 1, amount)

        return -1 if ans == float('inf') else ans