class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res,sol = [], []
        n = len(nums)

        def dfs(i,sol):
            res.append(sol.copy())
            for j in range(i,n):
                if j>i and nums[j]==nums[j-1]:
                    continue
                sol.append(nums[j])
                dfs(j+1,sol)
                sol.pop()
        dfs(0,sol)
        return res