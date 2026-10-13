class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        n = len(nums)
        used = [False]*n
        def dfs():
            nonlocal sol
            if len(sol) == n:
                res.append(sol.copy())
                return
            
            for i in range(n):
                if not used[i]:
                    sol.append(nums[i])
                    used[i] = True
                    dfs()
                    sol.pop()
                    used[i] = False


        dfs()
        return res