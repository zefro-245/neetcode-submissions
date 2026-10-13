class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int: #Memoization: Top Down
        n = len(cost) 
        dp = [-1]*(n+1)
        
        def f(i):
            if i==0:
                return cost[0]
            if i<0:
                return 0

            if dp[i]!=-1:
                return dp[i]
            
            dp[i] = cost[i]+min(f(i-1),f(i-2))
            return dp[i]

        return min(f(n-1),f(n-2))