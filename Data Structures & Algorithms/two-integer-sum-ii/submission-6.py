class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r = len(numbers)-1
        res = []
        while l<r:
            currsum = numbers[l]+numbers[r]
            if currsum==target:
                return [l+1,r+1]
            elif currsum<target:
                l+=1
            elif currsum>target:
                r-=1
   
