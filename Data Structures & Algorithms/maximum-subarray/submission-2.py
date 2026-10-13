class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [[None]*2 for _ in range(len(nums))]

        def f(i,flag):
            if i==len(nums)-1:
                if flag:
                    return max(0,nums[i])
                else:
                    return nums[i]
            if dp[i][flag] is not None:
                return dp[i][flag]
            
            if flag:
                dp[i][flag] = max(0,nums[i]+f(i+1,True))
            else:
                dp[i][flag] = max(f(i+1,False),nums[i]+f(i+1,True))
            
            return dp[i][flag]
        return f(0,False)