class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        after = [0] * 2 
        afterafter = [0] * 2 

        for ind in range(n-1,-1,-1):
            curr = [0] * 2 
            for buy in range(2):
                if buy:
                    curr[buy] = max(-prices[ind]+after[0],after[1])
                else:
                    curr[buy] = max(prices[ind]+afterafter[1],after[0])
                
            afterafter = after
            after = curr

        return curr[1]