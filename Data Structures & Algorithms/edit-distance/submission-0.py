class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        m, n = len(word1), len(word2)
        
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Base cases
        for i in range(m + 1):
            dp[i][n] = m - i   # delete remaining
        
        for j in range(n + 1):
            dp[m][j] = n - j   # insert remaining
        
        # Fill table bottom-up
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i][j + 1],     # insert
                        dp[i + 1][j],     # delete
                        dp[i + 1][j + 1]  # replace
                    )
        
        return dp[0][0]

        