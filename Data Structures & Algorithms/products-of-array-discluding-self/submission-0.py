class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        for i in nums:
            new = nums.copy()
            new.remove(i)
            prod = 1
            for j in new:
                prod = prod*j
            out.append(prod)
        return out
        