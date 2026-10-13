class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[-1]*len(word2) for _ in range(len(word1))]

        def f(i,j):
            if i<0:
                return j+1
            if j<0:
                return i+1
            if dp[i][j] != -1:
                return dp[i][j]
            eq = float("inf")
            if word1[i]==word2[j]:
                eq=0+f(i-1,j-1)
            ins = 1 + f(i,j-1)
            rep = 1 + f(i-1,j-1)
            dele = 1 + f(i-1,j)
            dp[i][j] = min(eq,ins,rep,dele)

            return dp[i][j]
        
        return f(len(word1)-1, len(word2)-1)