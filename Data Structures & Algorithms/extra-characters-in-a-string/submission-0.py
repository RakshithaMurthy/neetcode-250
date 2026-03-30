class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        wordSet = set(dictionary)

        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            # option 1: skip character
            dp[i] = 1 + dp[i + 1]

            # option 2: match words
            for j in range(i + 1, n + 1):
                if s[i:j] in wordSet:
                    dp[i] = min(dp[i], dp[j])

        return dp[0]
