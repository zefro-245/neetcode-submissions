class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)/2
        dp = [[-1]*(int(target)+1) for _ in range(len(nums))]

        def f(i,target):
            if target == 0:
                return True
            if i==0:
                return nums[0]==target
            
            if dp[i][int(target)]!=-1:
                return dp[i][int(target)]
            
            nottake = f(i-1,target)
            take = False
            if target>=nums[i]:
                take = f(i-1,target-nums[i])
            dp[i][int(target)] = take or nottake
            return take or nottake
        return f(len(nums)-1,target)