class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        n = len(nums)
        seen = []

        def dfs(i):
            if i>=n:
                if Counter(sol) not in seen:
                    res.append(sol.copy())
                seen.append(Counter(sol))
                return
            
            sol.append(nums[i])
            dfs(i+1)

            sol.pop()
            dfs(i+1)
        dfs(0)
        return res