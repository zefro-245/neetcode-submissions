class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        nums1 = nums[1:]
        nums2 = nums[:-1]
        memo1 = {}
        memo2 = {}
        
        def f1(i):
            if len(nums1) == 0:
                return nums[0]
            if i >= n-1:
                return 0
            
            if i in memo1:
                return memo1[i]

            memo1[i] = max(f1(i+2)+nums1[i], f1(i+1))

            return memo1[i] 
        def f2(i):
            if len(nums2) == 0:
                return nums[0]
            if i >= n-1:
                return 0
            
            if i in memo2:
                return memo2[i]

            memo2[i] = max(f2(i+2)+nums2[i], f2(i+1))

            return memo2[i] 

        return max(f1(0),f2(0))