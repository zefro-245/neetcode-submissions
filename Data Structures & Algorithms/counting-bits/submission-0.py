class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for j in range(n+1):
            res = 0
            for i in range(32):
                if 1<<i & j:
                    res+=1
            ans.append(res)
        return ans
        