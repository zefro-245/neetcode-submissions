class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = {}
        
        def f(i,prev_ind):
            if i==n:
                return 0
            if (i,prev_ind) in dp:
                return dp[(i,prev_ind)]

            length = f(i+1,prev_ind)

            if nums[i]>nums[prev_ind] or prev_ind==-1:
                length = max(length,1 + f(i+1,i))

            dp[(i, prev_ind)] = length
            return length

        return f(0,-1)