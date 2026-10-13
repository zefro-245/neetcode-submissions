class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1]*(n)

        def f(i):
            if i>=n:
                return 0
            if dp[i]!=-1:
                return dp[i]
            
            dp[i] = max(f(i + 2) + nums[i], f(i + 1))

            return dp[i]

        return f(0)