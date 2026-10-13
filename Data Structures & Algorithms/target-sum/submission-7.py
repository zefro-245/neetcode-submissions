class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = {}
        def f(i,target):
            if target==0 and i==n:
                return 1
            if i==n:
                return 0
            
            if (i,target) in dp:
                return dp[(i,target)]

            dp[(i,target)] = f(i+1,target+nums[i])+f(i+1,target-nums[i])
            return dp[(i,target)]
        
        return f(0,target)