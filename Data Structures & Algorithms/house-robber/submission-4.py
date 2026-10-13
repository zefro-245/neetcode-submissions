class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1]*n
        dp[0] = nums[0]

        for i in range(1,n):
            left = dp[i-1]
            if i>1:
                right = nums[i] + dp[i-2]
            else:
                right = nums[i]
            dp[i] = max(right,left)
        return dp[n-1]