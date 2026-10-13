class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        nums1 = nums[1:]
        nums2 = nums[:-1]

        dp1 = [-1]*(n-1)
        dp1[0] = nums1[0]

        dp2 = [-1]*(n-1)
        dp2[0] = nums2[0]

        for i in range(1,n-1):
            if i>1:
                dp1[i] = max(dp1[i-2]+nums1[i],dp1[i-1])
                dp2[i] = max(dp2[i-2]+nums2[i],dp2[i-1])
            else:
                dp1[i] = max(nums1[i],dp1[i-1])
                dp2[i] = max(nums2[i],dp2[i-1])
        return max(dp1[n-2],dp2[n-2])
