class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        n = len(nums)
        used = [False]*n

        def dfs(sol):
            if len(sol)==n:
                res.append(sol.copy())
                return 
            
            for i in range(n):
                if not used[i]:
                    sol.append(nums[i])
                    used[i] = True
                    dfs(sol)
                    sol.pop()
                    used[i] = False
        dfs(sol)
        return res  
                    
        