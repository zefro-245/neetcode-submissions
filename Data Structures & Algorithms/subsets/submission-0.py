class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []
        def dfs(i):
            while i>=n:
                res.append(sol.copy())
                return res 
            
            sol.append(nums[i])
            dfs(i+1)

            sol.pop()
            dfs(i+1)
        dfs(0)
        return res
            
