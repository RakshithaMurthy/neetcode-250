from functools import lru_cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        @lru_cache(None)
        def dfs(i, j):
            
            # If pattern finished
            if j == len(p):
                return i == len(s)
            
            # Check if first character matches
            first_match = (
                i < len(s) and
                (p[j] == s[i] or p[j] == '.')
            )
            
            # If next char is '*'
            if j + 1 < len(p) and p[j + 1] == '*':
                return (
                    dfs(i, j + 2) or
                    (first_match and dfs(i + 1, j))
                )
            else:
                return first_match and dfs(i + 1, j + 1)
        
        return dfs(0, 0)
