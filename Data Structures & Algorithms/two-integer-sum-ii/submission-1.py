class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            comp = target - numbers[i]
            if comp in numbers:
                j = numbers.index(comp)
                if i != j: 
                    return [min(i+1, j+1), max(i+1, j+1)]
        return []
        