class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in nums:
                j = nums.index(comp)
                if i != j: 
                    return [min(i, j), max(i, j)]
        return []
        