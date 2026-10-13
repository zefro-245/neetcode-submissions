class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = {}

        def f(ind, t):
            if ind == len(nums):
                return 1 if t == target else 0

            if (ind, t) in dp:
                return dp[(ind, t)]

            dp[(ind, t)] = (
                f(ind + 1, t + nums[ind]) +
                f(ind + 1, t - nums[ind])
            )

            return dp[(ind, t)]

        return f(0, 0)