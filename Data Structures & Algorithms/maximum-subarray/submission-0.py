class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        curMin, curMax = 0, 0

        for num in nums:
            tmp = curMax + num
            curMax = max(num + curMax, num + curMin, num)
            curMin = min(tmp, num + curMin, num)
            res = max(res, curMax)
        return res