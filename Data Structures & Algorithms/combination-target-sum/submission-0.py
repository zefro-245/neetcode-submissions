class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        n = len(nums)
        def dfs(i, remaining):
            if remaining == 0:
                res.append(sol.copy())
                return
            if i>=n or remaining < 0:
                return 
            
            sol.append(nums[i])
            remaining -= nums[i]
            dfs(i,remaining)

            val = sol.pop()
            remaining += val
            dfs(i+1, remaining)

        dfs(0,target)
        return res
