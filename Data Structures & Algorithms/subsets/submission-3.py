class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        nums.sort()
        n = len(nums)

        def dfs(i):
            res.append(sol.copy())

            for j in range(i, n):

                sol.append(nums[j])
                dfs(j + 1)
                sol.pop()

        dfs(0)
        return res