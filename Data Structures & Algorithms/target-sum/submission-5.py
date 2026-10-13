class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        total = sum(nums)

        # target must be achievable
        if abs(target) > total:
            return 0

        # total - target must be even
        if (total - target) % 2 != 0:
            return 0

        subset_target = (total - target) // 2

        return isSum(nums, subset_target)

        
def isSum(nums, target):
    n = len(nums)

    dp = [[-1] * (target + 1) for _ in range(n)]

    def f(ind, t):

        # We have considered all numbers
        if ind == 0:
            if t == 0 and nums[0] == 0:
                return 2
            if t == 0 or nums[0] == t:
                return 1
            return 0

        if dp[ind][t] != -1:
            return dp[ind][t]

        notTake = f(ind - 1, t)

        take = 0
        if nums[ind] <= t:
            take = f(ind - 1, t - nums[ind])

        dp[ind][t] = take + notTake

        return dp[ind][t]

    return f(n - 1, target)