class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numbers = Counter(nums)
        for i in numbers:
            if numbers[i]==1:
                return i