class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        s2 = s[::-1]
        dp = [[-1]*(n+1) for _ in range (n+1)]

        max_len = 0
        end_idx = 0

        for j in range(n):
            dp[0][j] = 0
        for i in range(n):
            dp[i][0] = 0
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]

                    if dp[i][j] > max_len and i - dp[i][j] == n - j:
                        max_len = dp[i][j]
                        end_idx = i
                else:
                    dp[i][j] = 0
        
        return s[end_idx - max_len : end_idx]