class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * n
        
        # Here, dp[i] includes the cost of the step itself
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i in range(2, n):
            # To get through step i, we pay for step i, plus the cheapest path to get here
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
            
        # The top is technically one step past the last element in the array
        return min(dp[n-1], dp[n-2])