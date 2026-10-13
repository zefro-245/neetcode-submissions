class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        numdic = Counter(nums)
        for i in numdic:
            if numdic[i]>1:
                return i