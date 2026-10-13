class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # r = 0
        maxprof = 0
        for l in range(len(prices)-1):
            r = l + 1
            while r<len(prices):
                profit = prices[r] - prices[l]

                if profit > maxprof:
                    maxprof = profit
                
                r += 1

        return max(maxprof,0)