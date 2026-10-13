class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        dp = [[0] * 2 for _ in range(n + 2)]

        for ind in range(n - 1, -1, -1):
            for buy in range(2):

                if buy:
                    dp[ind][buy] = max(
                        -prices[ind] + dp[ind + 1][0],
                        dp[ind + 1][1]
                    )

                else:
                    dp[ind][buy] = max(
                        prices[ind] + dp[ind + 2][1],
                        dp[ind + 1][0]
                    )

        return dp[0][1]