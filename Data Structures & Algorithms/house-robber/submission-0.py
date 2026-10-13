class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def f(i):
            if i >= n:
                return 0
            
            if i in memo:
                return memo[i]

            memo[i] = nums[i] + max(f(i+2), f(i+3))

            return memo[i] 

        return max(f(0),f(1))