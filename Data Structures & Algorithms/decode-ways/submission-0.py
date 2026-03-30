class Solution:
    def numDecodings(self, s: str) -> int:
        
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        
        # dp[i+1] and dp[i+2]
        one_step = 1     # dp[n]
        two_step = 0     # dp[n+1] (conceptual)
        
        for i in range(n - 1, -1, -1):
            
            current = 0
            
            # Single digit valid?
            if s[i] != '0':
                current = one_step
                
                # Two digit valid?
                if i + 1 < n and 10 <= int(s[i:i+2]) <= 26:
                    current += two_step
            else:
                current = 0
            
            two_step = one_step
            one_step = current
        
        return one_step

        