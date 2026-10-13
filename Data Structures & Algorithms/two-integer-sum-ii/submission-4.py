class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        res = []
        while l<r:
            add = numbers[l]+numbers[r] 
            if add == target:
                res = [l+1,r+1]
                return res
            elif add < target:
                l+=1
            elif add > target:
                r-=1
        return res

