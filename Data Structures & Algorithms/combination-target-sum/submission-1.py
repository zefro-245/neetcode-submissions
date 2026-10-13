class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        n = len(nums)

        def dfs(i,tot):
            if tot == target:
                res.append(sol.copy())
                return

            if i >= n or tot > target:
                return
            sol.append(nums[i])
            tot+=nums[i]
            dfs(i,tot)

            val = sol.pop()
            tot-=val
            dfs(i+1,tot)
        dfs(0,0)
        return res