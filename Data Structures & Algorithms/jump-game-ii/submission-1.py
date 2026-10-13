class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float('inf')]*len(nums)
        def f(ind):
            if ind>=len(nums)-1:
                return 0
            if dp[ind]!=float('inf'):
                return dp[ind]
            for i in range(1,nums[ind]+1):
                dp[ind] = min(dp[ind], 1+f(ind+i))
            return dp[ind]
        return f(0)
