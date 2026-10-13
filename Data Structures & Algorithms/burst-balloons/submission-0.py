class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        a = []
        n = len(nums)
        a.append(1)
        for alpha in range(n):
            a.append(nums[alpha])
        a.append(1)

        dp = {}
        def f(i,j):
            if i>j:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            maxi = float('-inf')
            for k in range(i,j+1):
                cost = a[i-1]*a[k]*a[j+1]+f(i,k-1)+f(k+1,j)
                maxi = max(maxi,cost)
                dp[(i,j)] = maxi
            return maxi
        return f(1,n)

            