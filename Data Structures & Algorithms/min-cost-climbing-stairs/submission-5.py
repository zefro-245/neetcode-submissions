class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1]*(n+1)
        
        def f(i):
            if i>=n:
                return 0

            if dp[i]!=-1:
                return dp[i]
            
            dp[i] = cost[i]+min(f(i+1),f(i+2))
            return dp[i]

        return min(f(0),f(1))